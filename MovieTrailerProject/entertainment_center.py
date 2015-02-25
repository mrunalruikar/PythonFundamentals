__author__ = 'MR028042'
import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story 2",
                        "A Story of a Toys",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/c/c0/Toy_Story_2.jpg/220px-Toy_Story_2.jpg",
                        "https://www.youtube.com/watch?v=Lu0sotERXhI")

titanic = media.Movie("Titanic",
                      "Your Ship ain't floating",
                      "http://upload.wikimedia.org/wikipedia/en/thumb/2/22/Titanic_poster.jpg/220px-Titanic_poster.jpg",
                      "https://www.youtube.com/watch?v=5d9ILag7mRA")

tangled = media.Movie("Tangled",
                      "Too long hair's",
                      "http://upload.wikimedia.org/wikipedia/en/thumb/a/a8/Tangled_poster.jpg/220px-Tangled_poster.jpg",
                      "https://www.youtube.com/watch?v=ip_0CFKTO9E")

twelve_angry_men = media.Movie("12 Angry men",
                               "We have no clue",
                               "http://upload.wikimedia.org/wikipedia/en/thumb/9/91/12_angry_men.jpg/220px-12_angry_men.jpg",
                               "https://www.youtube.com/watch?v=A7CBKT0PWFA")

tsr = media.Movie("The Shawshank Redemption",
                  "Fear can hold you prisoner. Hope can set you free.",
                  "http://upload.wikimedia.org/wikipedia/en/thumb/8/81/ShawshankRedemptionMoviePoster.jpg/220px-ShawshankRedemptionMoviePoster.jpg",
                  "https://www.youtube.com/watch?v=NmzuHjWmXOc")

gravity = media.Movie("Gravity",
                      "Don't Let Go",
                      "http://upload.wikimedia.org/wikipedia/en/thumb/f/f6/Gravity_Poster.jpg/220px-Gravity_Poster.jpg",
                      "https://www.youtube.com/watch?v=OiTiKOy59o4")

movies = [toy_story, titanic, tangled, twelve_angry_men, tsr, gravity]

fresh_tomatoes.open_movies_page(movies)