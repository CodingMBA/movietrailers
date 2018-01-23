import fresh_tomatoes
import media

good_will_hunting = media.Movie("Good Will Hunting",
                        "Self-taught genius learns about life.",
                        "https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg",
                        "https://youtu.be/PaZVjZEFkRs")

the_dark_knight = media.Movie("The Dark Knight",
                     "Batman tries to foil the Joker's plan to destroy Gotham.",
                     "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                     "https://youtu.be/kmJLuwP3MbY")

the_matrix = media.Movie("The Matrix",
                         "Programmer Neo leads a revolution to free humanity from the matrix.",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://youtu.be/vKQi3bBA1y8")

top_gun = media.Movie("Top Gun",
                      "A cocky fighter pilot grows up.",
                      "https://upload.wikimedia.org/wikipedia/en/4/46/Top_Gun_Movie.jpg",
                      "https://youtu.be/qAfbp3YX9F0")

fight_club = media.Movie("Fight Club",
                          "A man embraces his primal instincts in a modern world.",
                          "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                          "https://youtu.be/SUXWAEX2jlg")
pulp_fiction = media.Movie("Pulp Fiction",
                           "A multi-strand, ultra-hip crime movie",
                           "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                           "https://youtu.be/s7EdQ4FqbhY")

movies = [good_will_hunting, the_dark_knight, the_matrix, top_gun, fight_club, pulp_fiction]
fresh_tomatoes.open_movies_page(movies)
