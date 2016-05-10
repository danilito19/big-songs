import glob
from hdf5 import *
from mrjob.job import MRJob
import heapq


'''
Find top 10 terms overall

MUST RUN THIS FILE WITH
python myfile.py  --jobconf mapreduce.job.reduces=1 input-file


'''
class Topk(MRJob):

    def mapper(self, __, line):

        artist_name, song_year, artist_terms, hot = line.split("|")
        for t in artist_terms.split(","):
            yield t.lower(), 1

    def combiner(self, term, counts):

        yield term, sum(counts)

    def reducer_init(self):
        '''
        '''
        k = []

        for i in range(10):
          k.append((i, ' '))

        heapq.heapify(k)
        self.counts = k

    def reducer(self, term, counts):
        '''
        Use the heap's minimum value and comopare to
        the current count. If current count is larger than
        heap's minimum value, swap them.
        '''

        c = sum(counts)
        min_v, min_term = self.counts[0]

        if c > min_v:
            heapq.heapreplace(self.counts, (c, term))


    def reducer_final(self):
        '''
        Yield term and counts for top 10 most appearing terms, in reverse order.
        '''

        self.counts.sort(reverse=True)
        for i in self.counts:
            yield i[0], i[1]

if __name__ == '__main__':

    Topk.run()




