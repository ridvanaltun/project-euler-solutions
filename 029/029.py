import time
start = time.time()

dump = []
for i in range(2, 101):
    for j in range(2, 101):
        dump.append(i**j)

dump = list(set(dump))

print(len(dump))

elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds")

# This code took: 0.017941951751708984 seconds
