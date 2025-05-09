import streamlit as st
from faiss_search import search_faiss, generate_summary
from filters import recommend_products

# Streamlit UI
st.title("🛍️ AI Shopping Assistant")

# User query input
user_query = st.text_input("Ask me anything about products...")

if user_query:
    # Get product recommendations
    recommendations = recommend_products(user_query, search_faiss)

    st.subheader("🔍 **Recommended Products**")

    if recommendations:
        # Generate and Display Summary (Only if there are multiple products)
        if len(recommendations) >= 1:
            summary = generate_summary(recommendations)
            if summary:  # Avoid displaying empty summary
                st.subheader("📝 **Summary**")
                st.write(summary)

    else:
        st.warning("🚫 No matching products found. Try adjusting your query or price range!")
