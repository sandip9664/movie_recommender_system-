# 🎬 Semantic Movie Recommender

A content-based recommendation engine that leverages **Sentence Transformers** to suggest movies based on their semantic meaning. It dynamically fetches real-time metadata and high-quality posters using the **OMDb API**.

---

## 🚀 Quick Start

### Clone & Enter
```bash
git clone https://github.com/your-username/movie-recommender.git && cd movie-recommender
Setup Environment
Create a .env file and add your OMDb key:

bash
OMDB_API_KEY=your_key_here
Install Dependencies
bash
pip install -r requirements.txt
Run API
bash
uvicorn main:app --reload
Run UI (Optional)
bash
streamlit run app.py
🛠️ How It Works
Embedding: Uses sentence-transformers to convert movie descriptions into 384-dimensional dense vectors.

Matching: Calculates Cosine Similarity between the user’s input and pre-computed embeddings stored in embeddings.pkl.

Enrichment: Dynamically calls the OMDb API to retrieve posters, IMDb ratings, and plot summaries for recommended movies.

Serving: A FastAPI backend delivers top results with live metadata to a Streamlit frontend.

📌 Tech Stack
Python (FastAPI, Streamlit, Sentence Transformers)

OMDb API for metadata & posters

Cosine Similarity for semantic matching

Pickle for embedding storage

🎯 Features
Semantic recommendations based on movie descriptions

Real-time enrichment with IMDb ratings and posters

Interactive UI with Streamlit

Fast and scalable API with FastAPI
