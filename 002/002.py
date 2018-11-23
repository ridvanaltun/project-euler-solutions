sum, a, b, f = 0, 0, 1, 0

while True:

	f = a + b

	if f % 2 == 0:
		sum += f

	if f > 4000000:
		break
	else:
		a = b
		b = f

print(sum)