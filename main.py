
from recommender.movie_recommender import MovieRecommender

def main():
    recommender = MovieRecommender("data/movies.csv")
    print("Recommendations for genre='Thriller', min_rating=8.5:")
    print(recommender.recommend(genre='Thriller', min_rating=8.5))

if __name__ == "__main__":
    main()
