from movies import Movie, IMovieFinder

data = [
    Movie(year=1972, name="The Lift", director="Robert Zemeckis"),
    Movie(year=1973, name="A Field of Honor", director="Robert Zemeckis"),
    Movie(year=1978, name="I Wanna Hold Your Hand", director="Robert Zemeckis"),
    Movie(year=1979, name="1941", director="Steven Spielberg"),
    Movie(year=1980, name="Used Cars", director="Robert Zemeckis"),
    Movie(year=1984, name="Romancing the Stone", director="Robert Zemeckis"),
    Movie(year=1985, name="Back to the Future", director="Robert Zemeckis"),
    Movie(year=1988, name="Who Framed Roger Rabbit", director="Robert Zemeckis"),
    Movie(year=1989, name="Back to the Future Part II", director="Robert Zemeckis"),
    Movie(year=1990, name="Back to the Future Part III", director="Robert Zemeckis"),
    Movie(year=1992, name="Death Becomes Her", director="Robert Zemeckis"),
    Movie(year=1992, name="Trespass", director="Walter Hill"),
    Movie(year=1994, name="Forrest Gump", director="Robert Zemeckis"),
    Movie(year=1996, name="Bordello of Blood", director="Gilbert Adler"),
    Movie(year=1997, name="Contact", director="Robert Zemeckis"),
    Movie(year=2000, name="What Lies Beneath", director="Robert Zemeckis"),
    Movie(year=2000, name="Cast Away", director="Robert Zemeckis"),
    Movie(year=2004, name="The Polar Express", director="Robert Zemeckis"),
    Movie(year=2007, name="Beowulf", director="Robert Zemeckis"),
    Movie(year=2009, name="A Christmas Carol", director="Robert Zemeckis"),
    Movie(year=2012, name="Flight", director="Robert Zemeckis"),
    Movie(year=2015, name="The Walk", director="Robert Zemeckis"),
    Movie(year=2015, name="Doc Brown Saves the World", director="Robert Zemeckis"),
    Movie(year=2016, name="Allied", director="Robert Zemeckis"),
    Movie(year=2018, name="Welcome to Marwen", director="Robert Zemeckis"),
    Movie(year=2020, name="The Witches", director="Robert Zemeckis"),
]

class MovieFinder(IMovieFinder):

    def find_all(self):
        return data
