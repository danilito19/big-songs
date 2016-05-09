import glob
from hdf5 import *
from mrjob.job import MRJob


### decades 0: 2000, decade 1: 2010 - 


class DecadeTerms(MRJob):

    def mapper(self, __, line):

        artist_name, song_year, artist_terms, hot = line.split("|")

        # this only yields words with years, does not yields the terms
        # of songs without years
        if int(song_year) in range(1920, 2020):
            decade = int(song_year[2:4])/10
            for t in artist_terms.split(","):
                yield decade, t.lower()

    def combiner(self, decade, terms):
        for t in terms:
            yield decade, t

    def reducer(self, decade, terms):
        yield decade, list(terms)


if __name__ == '__main__':

    ######################
    #change this to the dir where your data is
    #files = glob.glob("../samples/*.h5")

    # for f in files:
    #     print get_year_terms(f)

    #def get_all_data():
    DecadeTerms.run()




