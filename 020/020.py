factorial = 1
sum = 0

for i in range(1,101):
	factorial = factorial * i

for i in str(factorial):
	sum = sum + int(i)

print(sum)