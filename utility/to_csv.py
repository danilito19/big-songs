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

    name =  get_artist_name(h5)
    tags = "|".join(get_artist_mbtags(h5))
    year = get_year(h5)
    hottness = get_artist_hotttnesss(h5)
    song_hot = get_song_hotttnesss(h5)
    artist_terms = "|".join(get_artist_terms(h5))
    title = get_title(h5)
    dance = get_danceability(h5)
    duration = get_duration(h5)
    tempo = get_tempo(h5)
    fadeout = get_start_of_fade_out(h5)
    artist_familiarity = get_artist_familiarity(h5)
    artist_id = get_artist_id(h5)
    artist_playmeid = get_artist_playmeid(h5)
    artist_7_digitid = get_artist_7digitalid(h5)
    lat = get_artist_latitude(h5)
    lon = get_artist_latitude(h5)
    artist_loc = get_artist_location(h5)
    release = get_release(h5)
    release_7digitid = get_release_7digitalid(h5)
    song_id = get_song_id(h5)
    track_5digit = get_track_7digitalid(h5)
    sample_rate = get_analysis_sample_rate(h5)
    fadein = get_end_of_fade_in(h5)
    energy = get_energy(h5)
    key = get_key(h5)
    key_confidence = get_key_confidence(h5)
    loud = get_loudness(h5)
    mode = get_mode(h5)
    mode_confidence = get_mode_confidence(h5)
    tempo = get_tempo(h5)
    time_sig = get_time_signature(h5)
    time_sig_confidence = get_time_signature_confidence(h5)
    track_id = get_track_id(h5)
    artist_mbtags = get_artist_mbtags(h5)

    # seg_start = get_segments_start(h5)
    # seg_conf = get_segments_confidence(h5)
    # pitches = get_segments_pitches(h5)
    # timbre = get_segments_timbre(h5)
    # max_loud = get_segments_loudness_max(h5)
    # max_loud_time = get_segments_loudness_max_time(h5)
    # seg_loud_start = get_segments_loudness_start(h5)
    # sec_start = get_sections_start(h5)
    # sec_conf = get_sections_confidence(h5)
    # beats_start = get_beats_start(h5)
    # beats_conf = get_beats_confidence(h5)
    # bars_start = get_bars_start(h5)
    # bars_conf = get_bars_confidence(h5)
    # tatums_start = get_tatums_start(h5)
    # tatums_conf = get_tatums_confidence(h5)
    #mbtags_count = get_artist_mbtags_count(h5)


    h5.close()

    return [name, title, year, artist_terms, song_id, hottness, tags, 
    dance, duration, tempo, fadeout, song_hot,
    artist_familiarity, artist_id, artist_playmeid, artist_7_digitid, 
    lat, lon, artist_loc, release, release_7digitid, song_id, track_5digit, sample_rate, 
    fadein, energy, key, key_confidence, loud, mode, mode_confidence, tempo, time_sig, 
    time_sig_confidence, track_id, artist_mbtags]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print '%s <inputfile> : parse out an input HDF5 file into text string' % sys.argv[0]
        sys.exit(2)

    folder = sys.argv[1]
    output = sys.argv[2]

    with open(output, 'wb') as csvfile:
        writer = csv.writer(csvfile)

        for root, dirnames, filenames in os.walk(folder):
            for filename in fnmatch.filter(filenames, '*.h5'):
                song = parse_file(os.path.join(root, filename))
                writer.writerow(song)

