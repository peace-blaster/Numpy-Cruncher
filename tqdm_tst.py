from tqdm import tqdm
from multiprocessing.pool import ThreadPool
import numpy

def cubes(bla):
    return sum(sum(sum(numpy.random.rand(1000,1000,1000))))

def IOLoop():
    try:
        calc(int(input('\nInput number of iterations to test: ')), int(input('\nInput number of threads for Pool: ')))
    except:
        print('\nInvalid input, try again.\n')
        IOLoop()

def calc(tst_len, threads):
    print('\n')
    for _ in tqdm(
        ThreadPool(threads).imap_unordered(cubes, range(tst_len)),
        total=tst_len,
        desc=f"Processing...",
    ):
        pass

desc = '''
/*=========================================================================*\\
|| NUMPY CRUNCHER DATA SCIENCE TEST v0.1                                   ||
|| ------------------------------------------------------------------------||
|| Creates and sums over large arrays to stress CPU with matrix operations ||
\\*=========================================================================*/
'''
# entrypoint:
print('\n'+desc+'\n')
IOLoop()