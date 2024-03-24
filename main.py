#!/usr/bin/env python

from lister import MovieLister

if __name__ == '__main__':
    lister = MovieLister()
    spielberg_movies = lister.movies_directed_by('Steven Spielberg')
    print(spielberg_movies)
