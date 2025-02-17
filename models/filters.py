import re

def extract_price_range(query):
    """Extracts a price range from user query, supporting both $ and ₹ (e.g., 'under ₹1000', 'above 500', 'between ₹500 and ₹1000')."""
    query = query.lower()  

    # Match patterns like "under ₹1000", "above ₹500", "below 200"
    match = re.search(r"(\bunder\b|\babove\b|\bbelow\b)?\s?[₹$]?\s?(\d+)", query, re.IGNORECASE)

    if match:
        condition = match.group(1)  # 'under', 'above', 'below'
        price = int(match.group(2))  

        if condition in ["under", "below"]:
            return ("max", price)  
        elif condition == "above":
            return ("min", price)  

    # Match patterns like "between ₹500 and ₹1000"
    match_between = re.search(r"between\s?[₹$]?\s?(\d+)\s?(and|-)\s?[₹$]?\s?(\d+)", query, re.IGNORECASE)
    if match_between:
        min_price = int(match_between.group(1))
        max_price = int(match_between.group(3))
        return ("range", (min_price, max_price))

    # Handle high-end products
    high_end_keywords = ["high-end", "luxury", "premium", "flagship", "expensive"]
    if any(word in query for word in high_end_keywords):
        return ("min", 200000)  # Adjusted for INR

    return None  

def recommend_products(user_query, search_faiss):
    """Recommend products using FAISS search with optional price filtering."""
    price_filter = extract_price_range(user_query)  

    # Set default price range
    min_price = 0
    max_price = float("inf")

    if price_filter:
        filter_type, value = price_filter
        if filter_type == "max":
            max_price = value  
        elif filter_type == "min":
            min_price = value  
        elif filter_type == "range":
            min_price, max_price = value  

    # 🔹 Search FAISS
    results = search_faiss(user_query, price=min_price, top_k=5)

    # 🔹 Apply post-filtering
    filtered_results = [p for p in results if min_price <= p["actual_price"] <= max_price]

    # 🔹 If no results after filtering, relax the price condition slightly
    if not filtered_results:
        relaxed_min = max(0, min_price * 0.8)  # Allow 20% lower price
        relaxed_max = max_price * 1.2  # Allow 20% higher price
        filtered_results = [p for p in results if relaxed_min <= p["actual_price"] <= relaxed_max]

    return filtered_results if filtered_results else results

