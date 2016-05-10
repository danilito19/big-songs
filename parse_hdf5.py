import sys
from hdf5 import *

def parse_file(file_path):
    '''
    Grabs song attributes

    ADD ADDITIONAL ATTRIBUTES!!

    MUST BE STRINGS
    '''
    h5 = open_h5_file_read(file_path)
    year = get_year(h5)
    terms = get_artist_terms(h5)
    name =  get_artist_name(h5)
    # no_t = get_artist_terms_freq(h5)
    # w = get_artist_terms_weight(h5)
    # tags = get_artist_mbtags(h5)
    hottness = get_artist_hotttnesss(h5)
    h5.close()
    artist_terms = ",".join(terms)

    return "|".join([name, str(year), artist_terms, str(hottness)])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print '%s <inputfile> : parse out an input HDF5 file into text string' % sys.argv[0]
        sys.exit(2)
    parse_file(sys.argv[1])
