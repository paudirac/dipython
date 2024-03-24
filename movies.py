import abc
import typing
from dataclasses import dataclass

@dataclass
class Movie:
    name: str
    director: str
    year: int


class IMovieFinder(abc.ABC):

    @abc.abstractmethod
    def find_all(self) -> typing.List[Movie]:
        pass
