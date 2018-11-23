num, i = 600851475143, 1

while True:
	if(num % i == 0):
		num = num/i
		if i>num:
			break
	i += 1
print(i)