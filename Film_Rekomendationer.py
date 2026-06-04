"""
Movies that the bot can recommend based on genre, mood, and age rating.
"""
movies = [
    {"title": "Inception", "genre": "Sci-Fi", "mood": "Mind-Blowing", "age": "13+"},
    {"title": "Interstellar", "genre": "Sci-Fi", "mood": "Emotional", "age": "13+"},
    {"title": "The Dark Knight", "genre": "Action", "mood": "Thrilling", "age": "13+"},
    {"title": "Avengers: Endgame", "genre": "Action", "mood": "Epic", "age": "13+"},
    {"title": "Titanic", "genre": "Romance", "mood": "Love", "age": "11+"},
    {"title": "La La Land", "genre": "Romance", "mood": "Emotional", "age": "11+"},
    {"title": "Frozen", "genre": "Animation", "mood": "Fun", "age": "0+"},
    {"title": "Toy Story", "genre": "Animation", "mood": "Fun", "age": "0+"},
    {"title": "The Lion King", "genre": "Animation", "mood": "Adventure", "age": "7+"},
    {"title": "Finding Nemo", "genre": "Animation", "mood": "Adventure", "age": "0+"},
    {"title": "The Conjuring", "genre": "Horror", "mood": "Scary", "age": "15+"},
    {"title": "It", "genre": "Horror", "mood": "Scary", "age": "15+"},
    {"title": "A Quiet Place", "genre": "Horror", "mood": "Suspenseful", "age": "15+"},
    {"title": "John Wick", "genre": "Action", "mood": "Intense", "age": "15+"},
    {"title": "Mission: Impossible", "genre": "Action", "mood": "Exciting", "age": "13+"},
    {"title": "The Hangover", "genre": "Comedy", "mood": "Funny", "age": "15+"},
    {"title": "Superbad", "genre": "Comedy", "mood": "Funny", "age": "15+"},
    {"title": "Forrest Gump", "genre": "Drama", "mood": "Heartwarming", "age": "11+"},
    {"title": "The Shawshank Redemption", "genre": "Drama", "mood": "Inspiring", "age": "15+"},
    {"title": "Spider-Man: Into the Spider-Verse", "genre": "Animation", "mood": "Exciting", "age": "7+"}
]


"""
This runs the recommendation system. It asks for the users prefrences by asking three questions. It then goes through the list of movies and gives a score which matches the users prefrences.
Then prints three recommendations based on the score. If the bot gets a score of 0 it will print that it doesnt have any recommendations. But if it prints three recommendations or more, then it asks the user if they like the recommendations and gives a response based on the users answer.
Finally it asks if the user would like another recommendation and based on the users answer it either runs the system again or says goodbye and ends the program.
"""
def run_recommendations():
    while True:
        genre = input("Which genre do you prefer? ").strip()
        mood = input("Which mood would you prefer? ").strip()
        age = input("What age rating do you prefer? ").strip()

        recommendations = 0

        for movie in movies:
            score = 0

            if genre and movie["genre"].lower() == genre.lower():
                score += 2

            if mood and movie["mood"].lower() == mood.lower():
                score += 2

            if age and movie["age"].lower() == age.lower():
                score += 1

            if score >= 1:
                print(f"{movie['title']} (score: {score})")
                print("-" * 47)
                recommendations += 1

            if recommendations == 3:
                break

        if recommendations == 0:
            print("No recommendations found for those preferences.")

        feedback = input("Do you like the recommendations? (yes/no): ")

        if feedback == "yes".strip().lower():
            print("Great! I will look for similar recommendations next time.")
        else:
            print("Okay, I will recommend something else next time.")

        again = input("Would you like another recommendation? (yes/no) ").strip().lower()
        if again == "no":
            print("Goodbye!")
            break


"""
This is the function that runs the recommendation system. Which is called in the main function.
"""
if __name__ == "__main__":
    run_recommendations()
