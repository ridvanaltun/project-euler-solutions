import time
start = time.time()

chain, max_num, max_chain, num  = 0, 0, 0, 0
for i in range(1,1000000):

	num = i

	while True:

		if num % 2 == 0:
			chain = chain + 1
			num = num/2
		else:
			if num == 1:
				if chain>max_chain:
					max_num = i
					max_chain = chain
				break
			else:
				chain = chain + 1
				num = (3 * num) + 1

	chain = 0
	num = 0

print("Max Chain Count  : "+max_chain)
print("Max Number 		: "+max_num)

elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds")

# 54.14922595024109 seconds