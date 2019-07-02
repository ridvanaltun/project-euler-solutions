"""

Asal sayıların tespiti için 10. soruda kullandığım
Erotosten Kalbburu adındaki algoritmayı kullanıyorum.

Öncelikle bir milyon asal sayıyı Erotosten ile haritalandırmak gerekiyor.
Böylelikle permütasyon işlemi sonrası asal sayı haritasından yararlanabiliriz.

"""

import time
start = time.time()

count = 0
num = 1000000
primes_map = [True] * num


def rotr(string, n):
    return string[n:] + string[:n]


def is_circular_prime(lst):
    for num in lst:
        if primes_map[num] is False:
            return False
    return True


# Asal sayılar haritalandır
for i in range(2, num):
    # asal sayı çıktı
    if primes_map[i]:
        # asal sayının tüm katlarını asal değildir diye işaretliyoruz
        for j in range(i * i, num, i):
            primes_map[j] = False


lst = []

# Dairesel asal sayıları say
for i in range(2, num):
    # Asal sayı
    if primes_map[i]:

        lst = []

        for j in range(len(str(i))):
            lst.append(int(rotr(str(i), j)))

        if is_circular_prime(lst):
            count = count + 1

# Sonucu yazdır
print(count)

elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds")

# This code took: 0.9156365394592285 seconds
