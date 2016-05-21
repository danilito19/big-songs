import glob
from mrjob.job import MRJob
import heapq


'''
Find the count of songs per year, including songs with no year

'''
class SongsPerYear(MRJob):

    def mapper(self, __, line):

        artist_name, song_year, artist_terms, hot = line.split("|")
        yield song_year, 1

    def combiner(self, year, counts):

        yield year, sum(counts)


    def reducer(self, year, counts):
        '''
        '''

        yield year, sum(counts)


if __name__ == '__main__':

    SongsPerYear.run()




