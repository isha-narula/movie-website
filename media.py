import webbrowser


class Movie():

    valid_ratings = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_t, movie_storyl, poster_image, trailer_youtube):
        self.title = movie_t
        self.storyline = movie_storyl
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
