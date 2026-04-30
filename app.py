import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="Movie Recommender System", layout="wide")

st.title("Movie Recommender System")

# Input for movie title
movie_title = st.text_input("Enter a movie title to get recommendations:")

if st.button("Recommend"):
    if movie_title:
        with st.spinner("Fetching recommendations..."):
            try:
                # Call the FastAPI backend
                response = requests.get(f"http://127.0.0.1:8000/recommend/{movie_title}")
                
                if response.status_code == 200:
                    recommendations = response.json()
                    
                    if not recommendations:
                        st.warning("No recommendations found.")
                    else:
                        st.success(f"Found {len(recommendations)} recommendations!")
                        
                        for movie in recommendations:
                            # Create a container for each movie
                            with st.container():
                                st.markdown("---")
                                # Create two columns: Left for details (wider), Right for poster (narrower)
                                col1, col2 = st.columns([2, 1])
                                
                                with col1:
                                    st.subheader(movie.get("Title", "Unknown Title"))
                                    st.write(f"**Year:** {movie.get('Year', 'N/A')}")
                                    st.write(f"**Rated:** {movie.get('Rated', 'N/A')}")
                                    st.write(f"**Runtime:** {movie.get('Runtime', 'N/A')}")
                                    st.write(f"**Genre:** {movie.get('Genre', 'N/A')}")
                                    st.write(f"**Director:** {movie.get('Director', 'N/A')}")
                                    st.write(f"**Actors:** {movie.get('Actors', 'N/A')}")
                                    st.write(f"**IMDb Rating:** {movie.get('imdbRating', 'N/A')}")
                                    
                                    st.markdown("### Plot")
                                    st.write(movie.get("Plot", "No plot available."))
                                    
                                with col2:
                                    poster_url = movie.get("Poster", "N/A")
                                    if poster_url != "N/A" and poster_url.startswith("http"):
                                        st.image(poster_url, use_container_width=True)
                                    else:
                                        st.info("No Poster Available")
                                        
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
                    
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a movie title.")
