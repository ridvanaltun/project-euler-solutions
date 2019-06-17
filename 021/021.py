import time
start = time.time()

a, b, c, num, total = 0, 0, 0, 0, 0
amicable = []

while True:

    num = num + 1

    for x in range(1, num):

        if num % x == 0:
            a += x

    # print("A = "+ str(a))

    for t in range(1, a):

        if a % t == 0:
            b += t

    # print("B = " +str(b))

    for r in range(1, b):

        if b % r == 0:
            c += r

    # print("C = " +str(c))

    # a ile c yi karşılaştırıp a ile b yi topluyoruz
    # a != b çünkü 6, 28 gibi sayılar amicable number sayılmıyor kendinlerini
    # tekrar ettikleri için

    if a == c and a != b:

        if a > 10000 or b > 10000:
            break

        amicable.append(a)
        amicable.append(b)

        total = total + a + b

    a = 0
    b = 0
    c = 0

# bazı değerler kendini tekrarlıyor, dublicate değerleri kullanmıyoruz
amicable = list(set(amicable))
print(sum(amicable))

elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds")

# 19.820363998413086 seconds
