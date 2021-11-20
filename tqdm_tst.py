from tqdm import tqdm
from multiprocessing.pool import ThreadPool
import numpy
from functools import partial

def cubes(intensity, bla):
    print(f'running at intensity {intensity}')
    return sum(sum(sum(numpy.random.rand(10*intensity,10*intensity,10*intensity))))

def intensityTestLoop():
    try:
        int(input('\nSelect test intensity (0 to 10): '))
    except:
        print('\n Expecting value between 0 and 10 \n')
        intensityTestLoop()

def IOLoop():
    try:
        calc(intensityTestLoop()
            , int(input('\nInput number of iterations to test: '))
            , int(input('\nInput number of threads for Pool: ')))
    except:
        print('\nInvalid input, try again.\n')
        IOLoop()

def calc(intensity, tst_len, threads):
    print('\n')
    func = partial(cubes, intensity)
    for _ in tqdm(
        ThreadPool(threads).imap_unordered(func, range(tst_len)),
        total = tst_len,
        desc = f'Processing...',
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
print('\n' + desc + '\n')
IOLoop()