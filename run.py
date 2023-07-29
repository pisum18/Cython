import compute
import compute_pure

if __name__ == "__main__":
    result = compute.determine_speed(1000)
    print("result is ", result)

    result2 = compute_pure.determine_speed(1000)
    print("result2 is ", result2)

    factor = result2 / result

    if (factor < 1):
        print("Cython is ", factor, "X slower than Python")
    elif (factor == 1):
        print("Cython and Python are the same speed")
    elif (factor > 1):
        print("Cython is ", factor, "X faster than Python")
