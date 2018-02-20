import media
import fresh_tomatoes

padmavaat = media.Movie("Padmavaat",
                        "Story of brave queen.",
                        "pic1.jpg",
                        "https://www.youtube.com/watch?v=8YaF2m7hCx0")


Inception = media.Movie("Inception",
                        "A Thriller",
                        "pic2.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")


Three_idiots = media.Movie("Three idiots",
                           "Story of three college friends",
                           "threeidiots.jpg",
                           "https://www.youtube.com/watch?v=xvszmNXdM4w")


The_fault_in_our_stars = media.Movie(
                                "The fault in our stars",
                                "American romantic director film",
                                "fault in our stars.jpg",
                                "https://www.youtube.com/watch?v=9ItBvH5J6ss")

Hunger_games = media.Movie(
    "Hunger games",
    "American post-apocalyptic science fiction action adventurous film",
    "hunger.jpg",
    "https://www.youtube.com/watch?v=mfmrPu43DF8")
Hangover = media.Movie("Hangover",
                       "Comedy film",
                       "hangover.jpg",
                       "https://www.youtube.com/watch?v=TZc39afdeXU")

# Creating an array called movies and store the Movie objects in that list.
movies = [
            padmavaat, Inception, Three_idiots,
            The_fault_in_our_stars, Hunger_games, Hangover]

# using the python program fresh tomatoes for opening our website.
fresh_tomatoes.open_movies_page(movies)
