import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# Load Data
movies = pd.read_csv("movies.csv")  # Make sure the CSV is in the same folder

# Clean title
def clean_title(title):
    return re.sub("[^a-zA-Z0-9 ]", "", title)

movies["clean_title"] = movies["title"].apply(clean_title)

# Vectorize
vectorizer = TfidfVectorizer(ngram_range=(1,2))
tfidf = vectorizer.fit_transform(movies["clean_title"])

# Search function
def search(title):
    title = clean_title(title)
    query_vec = vectorizer.transform([title])
    similarity = cosine_similarity(query_vec, tfidf).flatten()
    indices = similarity.argsort()[-5:][::-1]
    return movies.iloc[indices][["title", "genres"]]

# --- Streamlit UI ---
st.set_page_config(page_title="🎥 Movie Recommender", layout="centered")
st.title("🎬 Movie Recommendation Engine")
st.write("Type a movie name to get similar recommendations.")

movie_input = st.text_input("Enter a movie title:", "The Matrix")

if st.button("Recommend"):
    with st.spinner("Searching..."):
        results = search(movie_input)
        st.subheader("Top Recommendations:")
        for idx, row in results.iterrows():
            st.markdown(f"**🎞️ {row['title']}**  \n*Genre:* {row['genres']}  \n---")
