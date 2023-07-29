import Cython
import random
import timeit

def mainLoop(endHere = 1000):
    

    stopNow = endHere
    #cdef float stopNow
    running = True
    largeNumber = 0
    #cdef bint running = True

    #cdef float largeNumber = 0
    while running:
        if (largeNumber >= stopNow):
            running = False

        largeNumber += random.randint(0, 1)

def test_perf(iterations, stopNow):

    timer = timeit.timeit("mainLoop", globals=globals(), number = iterations)
    return timer

if __name__ == "__main__":
    print("hello world")

    stopNow = 1000
    
    timer = timeit.timeit("mainLoop(stopNow)", globals=globals(), number=1000)
    print("It took ", timer, " seconds")
