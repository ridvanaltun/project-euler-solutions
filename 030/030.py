count, tmp, sum = 2, 0, 0

try:
    while True:

        for i in str(count):
            tmp = tmp + int(i)**5

        if tmp == count:
            sum = sum + tmp
            print(count)

        tmp = 0
        count = count + 1

except KeyboardInterrupt:
    print("Sum is", sum)
