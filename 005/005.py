a = 1
done = False
list = [3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19]

while not done:
    if a % 10 == 0:
        for i in list:
            if a % i == 0:
                if i == 19:
                    done = True
                    print(a)
            else:
                break
    a += 1
