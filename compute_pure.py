import random
import timeit

def mainLoop(stopNow = 1000):
    
    running = True
    largeNumber = 0

    while running:
        if (largeNumber >= stopNow):
            running = False

        largeNumber += random.randint(0, 1)

def test_perf(iterations, stopNow):
    timer = timeit.timeit(mainLoop, number = iterations)
    return timer

if __name__ == "__main__":
    print("hello world")

    stopNow = 1000
    
    timer = timeit.timeit("mainLoop(stopNow)", globals=globals(), number=1000)
    print("It took ", timer, " seconds")
