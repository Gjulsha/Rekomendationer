"""
Movies that the bot can recommend based on genre, mood, and age rating.
"""
movies = [
    {"title": "The Shawshank Redemption", "genre": "Drama", "mood": "Inspiring", "age": "15+"},
    {"title": "The Godfather", "genre": "Crime Drama", "mood": "Intense", "age": "15+"},
    {"title": "The Dark Knight", "genre": "Action", "mood": "Thrilling", "age": "13+"},
    {"title": "Forrest Gump", "genre": "Drama", "mood": "Heartwarming", "age": "11+"},
    {"title": "Inception", "genre": "Science Fiction", "mood": "Thought-Provoking", "age": "13+"},
    {"title": "Interstellar", "genre": "Science Fiction", "mood": "Emotional", "age": "13+"},
    {"title": "The Matrix", "genre": "Science Fiction", "mood": "Mind-Blowing", "age": "15+"},
    {"title": "Gladiator", "genre": "Historical Action", "mood": "Epic", "age": "15+"},
    {"title": "Titanic", "genre": "Romance", "mood": "Romantic", "age": "11+"},
    {"title": "The Lord of the Rings: The Fellowship of the Ring", "genre": "Fantasy", "mood": "Adventurous", "age": "11+"},

    {"title": "The Lord of the Rings: The Two Towers", "genre": "Fantasy", "mood": "Epic", "age": "13+"},
    {"title": "The Lord of the Rings: The Return of the King", "genre": "Fantasy", "mood": "Triumphant", "age": "13+"},
    {"title": "Star Wars: A New Hope", "genre": "Science Fiction", "mood": "Adventurous", "age": "7+"},
    {"title": "Avengers: Endgame", "genre": "Action", "mood": "Epic", "age": "13+"},
    {"title": "Spider-Man: Into the Spider-Verse", "genre": "Animation", "mood": "Energetic", "age": "7+"},
    {"title": "Top Gun: Maverick", "genre": "Action", "mood": "Adrenaline-Fueled", "age": "11+"},
    {"title": "John Wick", "genre": "Action", "mood": "Intense", "age": "15+"},
    {"title": "Mission: Impossible – Fallout", "genre": "Action", "mood": "Action-Packed", "age": "13+"},
    {"title": "Jurassic Park", "genre": "Adventure", "mood": "Exciting", "age": "11+"},
    {"title": "The Lion King", "genre": "Animation", "mood": "Adventurous", "age": "7+"},

    {"title": "Toy Story", "genre": "Animation", "mood": "Funny", "age": "0+"},
    {"title": "Finding Nemo", "genre": "Animation", "mood": "Cozy", "age": "0+"},
    {"title": "Frozen", "genre": "Animation", "mood": "Cheerful", "age": "0+"},
    {"title": "Shrek", "genre": "Animation", "mood": "Humorous", "age": "7+"},
    {"title": "Up", "genre": "Animation", "mood": "Heartwarming", "age": "7+"},
    {"title": "The Hangover", "genre": "Comedy", "mood": "Hilarious", "age": "15+"},
    {"title": "Home Alone", "genre": "Comedy", "mood": "Cheerful", "age": "7+"},
    {"title": "La La Land", "genre": "Romance", "mood": "Emotional", "age": "11+"},
    {"title": "The Conjuring", "genre": "Horror", "mood": "Scary", "age": "15+"},
    {"title": "A Quiet Place", "genre": "Horror", "mood": "Suspenseful", "age": "15+"}
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
