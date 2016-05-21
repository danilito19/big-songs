import sys
from hdf5 import *
import csv
import fnmatch
import os

def parse_file(file_path):
    '''
    Grabs song attributes

    ADD ADDITIONAL ATTRIBUTES!!

    MUST BE STRINGS
    '''
    h5 = open_h5_file_read(file_path)
    year = get_year(h5)
    
    name =  get_artist_name(h5)

    tags = get_artist_mbtags(h5)
    tags = "|".join(tags)

    hottness = get_artist_hotttnesss(h5)

    terms = get_artist_terms(h5)
    artist_terms = "|".join(terms)

    title = get_title(h5)

    dance = get_danceability(h5)
    duration = get_duration(h5)
    tempo = get_tempo(h5)
    fadeout = get_start_of_fade_out(h5)
    
    h5.close()
    return [name, title, str(year), artist_terms, str(hottness), tags, dance, duration, tempo, fadeout]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print '%s <inputfile> : parse out an input HDF5 file into text string' % sys.argv[0]
        sys.exit(2)

    folder = sys.argv[1]

    with open('output.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)

        for root, dirnames, filenames in os.walk(folder):
            for filename in fnmatch.filter(filenames, '*.h5'):
                print 'currently in file: ', os.path.join(root, filename)
                song = parse_file(os.path.join(root, filename))
                writer.writerow(song)

