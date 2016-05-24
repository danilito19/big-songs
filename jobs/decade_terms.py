import glob
from mrjob.job import MRJob


### decades 0: 2000, decade 1: 2010 - 

class DecadeTerms(MRJob):

    def mapper(self, __, line):
        line = line.split(",")
        song_year = line[2]
        artist_terms = line[3]

        # this only yields words with years, does not yields the terms
        # of songs without years
        if int(song_year) in range(1920, 2020):
            decade = int(song_year[2:4])/10
            for t in artist_terms.split("|"):
                yield decade, t.lower()

    def combiner(self, decade, terms):
        terms = set(terms)
        for t in terms:
            yield decade, t

    def reducer(self, decade, terms):
        terms = set(terms)
        yield decade, list(terms)


if __name__ == '__main__':

    DecadeTerms.run()




