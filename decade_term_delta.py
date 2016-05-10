import glob
from hdf5 import *
from mrjob.job import MRJob


### decades 0: 2000, decade 1: 2010 - 

## calculate delta, which is if words started appearing more
## in a certain decade than a previous decade

'''
FOR NOW THIS IS ONLY DECADE COUNTS per term
'''
class DecadeCounts(MRJob):

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

    def reducer_init(self):
        '''
        '''
        self.term_counts = {}

    def reducer(self, decade, terms):

        self.term_counts[decade] = {}
        for t in terms:
            self.term_counts[decade][t] = (self.term_counts[decade].get(t, 0) + 1)
        print self.term_counts

if __name__ == '__main__':

    DecadeCounts.run()




