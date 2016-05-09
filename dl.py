import glob
from hdf5 import *
from mrjob.job import MRJob

decades = {'1920': (1920, 1930),
        "1930": (1930, 1940),
        "1940": (1940, 1950),
        "1950": (1950, 1960),
        "1960": (1960, 1970),
        "1970": (1970, 1980),
        "1980": (1980, 1990),
        "1990": (1990, 2000),
        "2000": (2000, 2010),
        "2010": (2010, 2016)
    
}

### decades 0: 2000, decade 1: 2010 - 


class DecadeTerms(MRJob):

    def mapper(self, __, line):

        artist_name, artist_year, artist_terms, hot = line.split("|")

        for t in artist_terms.split(","):
            yield t.lower(), artist_year

    def combiner(self, term, year):
        for yr in year:
            if int(yr) in range(1920, 2020):
                decade = int(yr[2:4])/10
                yield term, decade


    def reducer(self, term, decade):
        # print term, list(decade)
        for d in decade:
            yield d, term


    # create a step and another reducer to give list of words per decade

if __name__ == '__main__':

    ######################
    #change this to the dir where your data is
    #files = glob.glob("../samples/*.h5")

    # for f in files:
    #     print get_year_terms(f)

    #def get_all_data():
    DecadeTerms.run()




