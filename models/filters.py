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

    # Handle high-end products
    high_end_keywords = ["high-end", "luxury", "premium", "flagship", "expensive"]
    if any(word in query for word in high_end_keywords):
        return ("min", 60000)  # Adjusted for INR

    return None  

def recommend_products(user_query, search_faiss):
    """Recommend products using FAISS search with optional price filtering."""
    price_filter = extract_price_range(user_query)

    # Default price range
    min_price = 0
    max_price = float("inf")

    # Apply extracted price filter
    if price_filter:
        filter_type, value = price_filter
        if filter_type == "max":
            max_price = value
        elif filter_type == "min":
            min_price = value

    # 🔹 Search FAISS
    results = search_faiss(user_query, price=min_price, top_k=5)

    # 🔹 Filter strictly by price
    filtered_results = [p for p in results if min_price <= p["actual_price"] <= max_price]

    # 🔹 Return strictly matched results only
    return filtered_results

