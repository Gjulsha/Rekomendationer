while True:
    genre = input ("Which genre do you prefer?")
    mood = input ("Which mood would you prefer?")
    age = input ("What age rating do you prefer?")

    movies =[
        {"title":"Spider-Man: No Way Home","genre":"Action","mood":"Exciting","age":"11+"},
        {"title":"Home Alone","genre":"Comedy","mood":"Nostalgia","age":"11+"},
        {"title":"Titanic","genre":"Drama","mood":"Tragedy","age":"11+"},
        {"title":"The Conjuring","genre":"Horror","mood":"Fear","age":"15+"},
        {"title":"Avatar","genre":"Sci-Fi","mood":"Breathtaking","age":"11+"},
        {"title":"The Notebook","genre":"Romance","mood":"Love","age":"15+"},
        {"title":"Shrek","genre":"Cartoon","mood":"Fun","age":"0+"},
        {"title":"Jurassic Park","genre":"Thriller","mood":"Thrill","age":"10+"},
        {"title":"Harry Potter and the Sorcerer's Stone","genre":"Fantasy","mood":"Gentle Adventure","age":"7+"},
        {"title":"The Godfather","genre":"Crime","mood":"Power","age":"15+"},
        ]

    best_score = 0
    best_movie = ""

    for movie in movies :
        score = 0

        if movie["genre"] == genre:
            score +=2
        if movie["mood"] == mood:
            score +=2
        if movie["age"] == age:
            score +=1

        if score > best_score:
            best_score = score
            best_movie = movie["title"]
        
            print("Rekomendation:", best_movie)

            again = input ("Would you like another recommendation? (yes/no) ")
            if again.lower().strip() != "yes":
                    break
