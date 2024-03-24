from finder import MovieFinder


class MovieLister:

    def __init__(self):
        self.finder = MovieFinder()

    def movies_directed_by(self, director):
        all_movies = self.finder.find_all()
        return [movie for movie in all_movies if movie.director == director]
