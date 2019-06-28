import time
start = time.time()

sum, tmp = 0, 0
ALPHABET = ['A', 'B', 'C', 'D',	'E', 'F', 'G', 'H',	'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Parse names from names.txt file
with open('names.txt', 'r') as f:
    names = f.read().split(',')

# Close names.txt file
f.close()

# Clear " characters in the name list
for i, name in enumerate(names):
    names[i] = name.replace('"', '')

# Sort names in alphabetical order
names.sort()

# Magic
for i, name in enumerate(names):
    for letter in name:
        for k, chr in enumerate(ALPHABET):
            if chr == letter:
                tmp = tmp + (k + 1)
                break
    sum = sum + (tmp * (i + 1))
    tmp = 0

# Print the result
print(sum)

elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds")

# This code took: 0.05326128005981445 seconds
