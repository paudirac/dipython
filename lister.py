import typing
import abc

from movies import Movie, IMovieFinder


class IMovieLister(abc.ABC):

    @abc.abstractmethod
    def movies_directed_by(self, director: str) -> typing.List[Movie]:
        pass


class MovieLister(IMovieLister):

    def __init__(self, finder: IMovieFinder):
        if finder is None:
            raise TypeError("finder canno't be None")
        if not isinstance(finder, IMovieFinder):
            raise TypeError("finder should be an IMovieFinder")
        self.finder = finder

    def movies_directed_by(self, director: str) -> typing.List[Movie]:
        all_movies = self.finder.find_all()
        return [movie for movie in all_movies if movie.director == director]
