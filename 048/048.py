import time
start = time.time()

sum = 0
for i in range(1, 1000):
    sum = sum + i**i

print(str(sum)[-10:])

elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds")

# This code took: 0.01562190055847168 seconds
