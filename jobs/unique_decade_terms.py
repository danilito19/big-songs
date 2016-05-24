import glob
from mrjob.job import MRJob


### decades 0: 2000, decade 1: 2010 - 

class UniqueDecadeTerms(MRJob):

    def mapper(self, __, line):
        line = line.split(",")
        song_year = line[2]
        artist_terms = line[3]

        # this only yields words with years, does not yields the terms
        # of songs without years
        if int(song_year) in range(1920, 2020):
            decade = int(song_year[2:4])/10
            for t in artist_terms.split("|"):
                yield t.lower(), decade

    def combiner(self, term, decades):
        decades = set(decades)
        for d in decades:
            yield term, d

    def reducer(self, term, decades):
        decades = set(decades)

        if len(list(decades)) == 1:
            yield term, list(decades)[0]


if __name__ == '__main__':

    UniqueDecadeTerms.run()




