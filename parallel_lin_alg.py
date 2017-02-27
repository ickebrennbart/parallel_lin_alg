import numpy as np
import matplotlib.pylab as plt
import time
from joblib import Parallel, delayed
import multiprocessing

''' Distributes dot product over multiple cores
    - x will be split along axis=0 into bins that match the number of cores
    - returns dot product of x*y
'''
def parallel_dot(x, y, par=None, cores=4):
    # print "parallel_dot...................."
    func = np.dot # change if different function desired
    xsize = x.shape[0]  # use this dimension to distribute across cores
    bins = np.linspace(0, xsize, cores+1).astype(int) # create bins of input data
    if par is None or cores == 1:
        res = func(x, y)
    else:
        results = par(delayed(func)(x[bins[i-1]:bins[i],:], y) for i in range(1, cores+1))
        res = np.zeros((x.shape[0], y.shape[1]))
        for i in range(1, cores+1):
            res[bins[i-1]:bins[i],:] = results[i-1]

    return res


''' example code comparing single and multi core performance '''
def example():
    rounds = 50
    res = np.zeros((rounds, 2))
    print "Single core \t Multi core"
    for i in range(1,rounds):
        ''' create random arrays '''
        a = np.random.rand(i*100, i*100)
        b = np.random.rand(i*100, i*100)

        ''' compute dot product on single core '''
        sc_start = time.time()
        c = np.dot(a,b)
        sc_end = time.time()

        ''' compute on multiple cores '''
        with Parallel(n_jobs=multiprocessing.cpu_count(), backend='threading') as par:
            c = parallel_dot(a,b, par, multiprocessing.cpu_count())
        mc_end = time.time()

        res[i] = [sc_end-sc_start, mc_end-sc_end]
        print sc_end-sc_start, mc_end-sc_end

    plt.plot(res)
    plt.show()

if __name__ == "__main__":
    example()
