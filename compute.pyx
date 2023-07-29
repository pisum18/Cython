import Cython
import numpy as np
import timeit
import time
import cProfile

def main():
    cdef int i, j, k
    k = 1000
    
    cdef int[1000] h
    #cdef int[1000] g

    g = [0]*1000


    for i in range(k):
        for j in range(k):
            g[i] = i * j

def determine_speed(iterations = 1000000):
    time_taken = timeit.timeit(main, number = iterations)
    return time_taken

if __name__ == "__main__":
    time_taken = timeit.timeit(main)
    print("time taken is", time_taken)

