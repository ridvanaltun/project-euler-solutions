import time
import math

start = time.time()

grid = 20


def central_binomals(n):
    return (math.factorial(2*n))/(math.factorial(n))**2


print(central_binomals(grid))

elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds")

# This code took: 0.0 seconds
