import glob
from hdf5 import *
from mrjob.job import MRJob




class DecadeTerms(MRJob):
  '''

  '''
  
  def mapper(self, __, line):
    '''
    '''
    artist_name, artist_year, artist_terms, hot = line.split("|")

    for t in artist_terms.split(","):
        yield hot, t

if __name__ == '__main__':

    ######################
    #change this to the dir where your data is
    #files = glob.glob("../samples/*.h5")

    # for f in files:
    #     print get_year_terms(f)

    #def get_all_data():
    DecadeTerms.run()




