def fac(num):
    tmp = 1
    sum = 0
    for digit in str(num):
        if digit == 0 or digit == 1:
            pass  # tmp hali hazırda 1 zaten
        else:
            for i in range(1, int(digit) + 1):
                tmp = tmp * i

        sum = sum + tmp
        tmp = 1
    return sum


num = 1
sum = 0

try:
    while True:

        if num == fac(num):
            print(num)
            sum = sum + num

        num = num + 1

except KeyboardInterrupt:
    # Soruda 1 ve 2 toplama dahil değil diyor
    print("Sum is", sum - 1 - 2)
