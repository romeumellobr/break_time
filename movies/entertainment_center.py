import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        )
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8",
                     )
matrix = media.Movie("Matrix",
                     "Neo is the ONE",
                     "https://upload.wikimedia.org/wikipedia/pt/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU",
                     )
movies = [toy_story, avatar, matrix]
fresh_tomatoes.open_movies_page(movies)
