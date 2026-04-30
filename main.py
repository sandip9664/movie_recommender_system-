from fastapi import FastAPI,HTTPException
import pickle
import pandas as pd
import requests
from fastapi.middleware.cors import CORSMiddleware
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import os


app=FastAPI(title="movie recommender system",version="0.0.1")

load_dotenv()
API_KEY=os.getenv("API_KEY")

try:
    with open('movies_df.pkl','rb') as f:
        df=pickle.load(f)
    
    with open('movie_embeddings.pkl','rb') as f:
        movie_embeddings=pickle.load(f)
except Exception as e:
    raise HTTPException(status_code=500,detail="error while opening pickle file")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)



indices = pd.Series(df.index, index=df['title'].fillna('').astype(str).str.lower()).to_dict()

@app.get("/")
def home():
    return {'message':'hello, this is movie recommender system api and it is running'}

@app.get("/recommend/{movie_title}")
def get_recommendation(movie_title:str):
    try:
        print(f"Received request for: {movie_title}")
        
        # Case-insensitive search
        found_title = None
        for title in indices.keys():
            if title.lower() == movie_title.lower():
                found_title = title
                break
        
        if not found_title:
            print("Movie not found in indices")
            raise HTTPException(status_code=400,detail='movie not found')
            
        print(f"Found title: {found_title}")
        idx=indices[found_title]
        print(f"Index: {idx}")

        print("Calculating cosine similarity...")
        cosine_sim=cosine_similarity([movie_embeddings[idx]], movie_embeddings).flatten()
        print("Cosine similarity calculated")

        sim_scores=sorted(list(enumerate(cosine_sim)),key=lambda x: x[1],reverse=True)

        sim_scores=sim_scores[1:31]

        movie_indices=[i[0] for i in sim_scores]

        movie_titles=df['title'].iloc[movie_indices].tolist()

        recommended_movies = []
        for title in movie_titles:
            if len(recommended_movies) >= 10:
                break

            data_url = f"https://www.omdbapi.com/?t={title}&apikey={API_KEY}"
            try:
                response = requests.get(data_url)
                data = response.json()
                
                if data.get("Response") == "True":
                    # User requested all data, so we append the full data dictionary
                    # Removing "Response" field as requested
                    data.pop("Response", None)
                    recommended_movies.append(data)
                else:
                    # Skip if movie not found in OMDb
                    print(f"Skipping {title}: Movie not found in OMDb")
                    continue
            except Exception as e:
                print(f"Error fetching data for {title}: {e}")
                continue

        return recommended_movies

    except Exception as e:
        print(f"Error in recommendation logic: {e}")
        raise HTTPException(status_code=500, detail=str(e))




