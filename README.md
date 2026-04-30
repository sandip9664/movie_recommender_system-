🎬 Semantic Movie Recommender : A content-based recommendation engine that uses Sentence Transformers to suggest movies based on their semantic meaning. It dynamically fetches real-time metadata and high-quality posters using the OMDb API.  
🚀 Quick StartClone & Enter:Bashgit clone https://github.com/your-username/movie-recommender.git && cd movie-recommender Setup Environment:
Create a .env file and add your key: OMDB_API_KEY=your_key_here. 
Install:Bashpip install -r requirements.txt
Run API:Bashuvicorn main:app --reload
Run UI (Optional):streamlit run app.py
🛠️ How It Works
Embedding: Uses sentence-transformers to turn movie descriptions into 384-dimensional dense vectors. 
Matching: Calculates Cosine Similarity between the user's input and the pre-computed embeddings in embeddings.pkl. 
Enrichment: Dynamically calls the OMDb API to retrieve posters, IMDB ratings, and plot summaries for the recommended movies. 
Serving: A FastAPI backend returns the top results with live metadata to a Streamlit frontend.  
