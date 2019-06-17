sq_sum, sum = 0, 0

for i in range(1, 101):
    sq_sum = sq_sum + (i * i)
    sum = sum + i

print((sum * sum) - sq_sum)
