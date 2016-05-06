import glob
from hdf5 import *
from mrjob.job import MRJob



def get_year_terms(song_file):

    h5 = open_h5_file_read(song_file)
    year = get_year(h5)
    terms = get_artist_terms(h5)
    #no_t = get_artist_terms_freq(h5)
    #w = get_artist_terms_weight(h5)
    tags = get_artist_mbtags(h5)
    h5.close()
    return year, terms


class H5Protocol(object):

    def read(self, h5):

        # receive opened (orn ot?) h5 file, get attributes and return them
        year, terms = get_year_terms(h5)
        print year, terms
        return year, terms

    def write(self, key, value):
        return key, value


class DecadeTerms(MRJob):
  '''

  '''
  INPUT_PROTOCOL = H5Protocol

  
  def mapper(self, key, val):
    '''
    '''
    print key
    print val
    yield key, val


if __name__ == '__main__':

    ######################
    #change this to the dir where your data is
    #files = glob.glob("../samples/*.h5")

    # for f in files:
    #     print get_year_terms(f)

    #def get_all_data():
    DecadeTerms.run()




