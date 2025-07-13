# movie-recommender
# 🎬 Movie Recommender

A simple Python-based movie recommendation system that filters movies by genre and minimum rating using a CSV dataset.

## 📂 Dataset
Located in `data/movies.csv`  
It contains columns:
- `movie`: Movie name
- `genre`: Genre of the movie (e.g. Drama, Action)
- `rating`: IMDb rating (float)

## 💡 How it works
The recommender reads the CSV and returns a list of movies matching:
- A given genre
- A minimum IMDb rating

## ▶️ Usage
```bash
python main.py
