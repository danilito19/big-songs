from mrjob.job import MRJob


'''
Find the count of songs per year, including songs with no year

'''
class SongsPerYear(MRJob):

    def mapper(self, __, line):

        line = line.split(",")
        song_year = line[2]
        yield song_year, 1

    def combiner(self, year, counts):

        yield year, sum(counts)


    def reducer(self, year, counts):

        yield year, sum(counts)


if __name__ == '__main__':

    SongsPerYear.run()




