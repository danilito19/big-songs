import glob
from hdf5 import *


'''
File to open sample songs data and access attributes through hdf5 getters

'''

def get_year_terms(song_file):

    h5 = open_h5_file_read(f)
    year = get_year(h5)
    terms = get_artist_terms(h5)
    #no_t = get_artist_terms_freq(h5)
    #w = get_artist_terms_weight(h5)
    tags = get_artist_mbtags(h5)
    h5.close()
    return year, terms

def list_all(maindir):
    """
    Goes through all subdirectories, open every song file,
    and list all artists it finds.
    It returns a dictionary of string -> tuples:
       artistID -> (musicbrainz ID, trackID, artist_name)
    The track ID is random, i.e. the first one we find for that
    artist. The artist information should be the same in all track
    files from that artist.
    We assume one song per file, if not, must be modified to take
    into account the number of songs in each file.
    INPUT
      maindir  - top directory of the dataset, we will parse all
                 subdirectories for .h5 files
    RETURN
      dictionary that maps artist ID to tuple (MBID, track ID, artist name)
    """
    results = {}
    numfiles = 0
    # iterate over all files in all subdirectories
    for root, dirs, files in os.walk(maindir):
        # keep the .h5 files
        files = glob.glob(os.path.join(root,'*.h5'))
        for f in files :
            numfiles +=1
            # get the info we want
            aid,ambid,tid,aname = get_artistid_trackid_artistname(f)
            assert aid != '','null artist id in track file: '+f
            # check if we know that artist
            if aid in results.keys():
                continue
            # we add to the results dictionary
            results[aid] = (ambid,tid,aname)
    # done
    return results


######################
#change this to the dir where your data is
files = glob.glob("../samples/*.h5")

for f in files:
    print get_year_terms(f)

#def get_all_data():




