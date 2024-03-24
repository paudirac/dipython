#!/usr/bin/env python

from lister import MovieLister
from finder import MovieFinder

if __name__ == '__main__':
    finder = MovieFinder()
    lister = MovieLister(finder=finder)
    spielberg_movies = lister.movies_directed_by('Steven Spielberg')
    print(spielberg_movies)
