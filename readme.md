# **AI-Powered Shopping Assistant 🛍️**  

This project is an AI-powered shopping assistant that recommends products based on user queries. It uses **sentence embeddings** and **FAISS** for fast similarity search. Additionally, it leverages **Large Language Models (LLMs)** to generate summaries from research, providing users with concise insights on products.  

---

## ✨ **Key Features**  

✅ **🔍 Smart Product Search** – Uses **FAISS** and **sentence embeddings** to find the most relevant products in real time.  
✅ **💰 Intelligent Price Filtering** – Supports queries like *"laptops under ₹50,000"*, *"best smartphones above ₹20,000"*, and *"between ₹10,000 and ₹15,000"*.  
✅ **📄 AI-Powered Summaries** – Extracts key insights from product descriptions and reviews using **LLMs** (like GPT).  
✅ **⚡ Lightning-Fast Recommendations** – FAISS ensures search speeds in **milliseconds**, even with **millions of products**.  
✅ **🎨 User-Friendly Interface** – Built with **Streamlit**, allowing a smooth, interactive shopping experience.  

---

## 📂 **Dataset**  

The project is built on real-world e-commerce data from Amazon:  
🔗 **[Amazon Products Dataset](https://www.kaggle.com/datasets/lokeshparab/amazon-products-dataset)**  

The dataset contains:  
- Product titles, descriptions, and categories  
- Pricing information  
- Ratings and customer reviews  

---

## 🛠️ **Tech Stack**  

### 🔹 **Machine Learning & NLP**  
- **FAISS** – Fast Approximate Nearest Neighbor Search  
- **Sentence Transformers** – Semantic similarity with embeddings  
- **Large Language Models (LLMs)** – Text summarization & insights  

### 🔹 **Backend & API**  
- **Python** – Core development  

### 🔹 **Frontend & Deployment**  
- **Streamlit** – Interactive UI for shopping assistant  

---

## 🚀 **Quick Start**  

```bash
# 1️⃣ Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Run the Streamlit app
streamlit run app.py
```

---

## 🔖 **Why This Project Stands Out?**  

🎯 **AI-Powered Shopping Assistant** – Not just a search engine, but a **smart assistant** with AI-driven insights.  
🤖 **State-of-the-Art NLP** – Uses **transformer models** to deeply understand user intent.  
💡 **Smart Price Filtering** – Handles queries like *"best budget laptops under ₹40,000"*.  
📊 **LLM-Based Summaries** – Extracts key insights from product reviews, so users make informed choices.  

---

## 📌 **Future Enhancements**  

🔗 **Multi-Vendor Support** – Compare products across **Amazon, Flipkart, and eBay**.  

---

💡 **This project is a great showcase of AI, NLP, and fast retrieval techniques, making it perfect for e-commerce and AI-driven applications!**  
