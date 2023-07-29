import compute
import compute_pure

if __name__ == "__main__":
    iterations = 10000

    stopNow = 1000

    result_C = compute.test_perf(iterations, stopNow)
    result_P = compute_pure.test_perf(iterations, stopNow)
    
    ratio = result_P / result_C
    if (ratio > 1):
        print("Python is ", ratio, " X slower than Cython")
    elif(ratio == 1):
        print("Python is just as fast as Cython")
    elif (ratio < 1):
        print("Python is ", ratio, " X faster than Cython")
