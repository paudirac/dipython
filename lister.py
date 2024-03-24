import typing

from movies import Movie, IMovieFinder


class MovieLister:

    def __init__(self, finder: IMovieFinder):
        self.finder = finder

    def movies_directed_by(self, director: str) -> typing.List[Movie]:
        all_movies = self.finder.find_all()
        return [movie for movie in all_movies if movie.director == director]
