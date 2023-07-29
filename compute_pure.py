import numpy as np
import timeit
import time
import pstats
import cProfile

def main():
    k = 1000
    
    h = []
    g = [0]*1000


    for i in range(k):
        for j in range(k):
            g[i] = i * j

def determine_speed(iterations = 1000000):
    time_taken = timeit.timeit(main, number = iterations)
    return time_taken

def profile_speed(iterations = 1000000):
    cProfile.runctx("determine_speed(iterations)", globals=globals(), locals=locals(), filename="determine_speed_stats")
    p = pstats.Stats("determine_speed_stats")
    p.sort_stats("cumulative").print_stats()


if __name__ == "__main__":

    # profile_speed(1000)
    iterations = 1000

    cProfile.runctx("determine_speed(iterations)", globals=globals(), locals=locals(), filename="determine_speed_stats")
    p = pstats.Stats("determine_speed_stats")
    p.sort_stats("cumulative").print_stats()
    
    # time_taken = timeit.timeit(main)
    # print("time taken is", time_taken)

