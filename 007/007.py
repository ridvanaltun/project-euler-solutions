import time
start = time.time()

count = 0
say= 0
prime = False

while True:
	say = say + 1
	for i in range(3,say,2):
		if say % i ==0 or say % 2 == 0:
			prime = False
			break
		else:
			prime = True
			
	if prime:
		count = count + 1

		if(count == 10001-2): # 2 ve 3 rakamları asal olarak alınmadığı için 2 geri gittik
			print(say)
			break

elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds")

# old -> 89.22042536735535 seconds
# new -> 66.05653405189514 seconds