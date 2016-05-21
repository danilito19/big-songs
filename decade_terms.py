import glob
from mrjob.job import MRJob


### decades 0: 2000, decade 1: 2010 - 

class DecadeTerms(MRJob):

    def mapper(self, __, line):
        print 'IN MAPPER'
        current_input = line.split("|")
        print current_input
        #artist_name, song_year, artist_terms, hot = line.split("|")
        print 'length of current_input is: ', len(current_input)
        # song_year = current_input[1]
        # artist_terms = current_input[2]

        # # this only yields words with years, does not yields the terms
        # # of songs without years
        # if int(song_year) in range(1920, 2020):
        #     decade = int(song_year[2:4])/10
        #     for t in artist_terms.split(","):
        #         yield decade, t.lower()

        yield 'dana', 1
    # def combiner(self, decade, terms):
    #     for t in terms:
    #         yield decade, t

    def reducer(self, decade, terms):
        yield 'dana', 1


if __name__ == '__main__':

    DecadeTerms.run()




