"""
Method: 1

Klasik brute force.
Sonucu bulması bir kaç saat sürüyor.

Bazı optimizasyonlar yaptım ama fayda etmedi, yaptığım optimizasyonlar:

Ucgensel sayı tek bir sayıysa çarpanlarını bulan döngüyü;
Ücgensel sayı/3 olunca bitir.

Ucgensel sayı cift bir sayıysa sayının çarpanlarını bulan döngüyü;
Sayı/2 olunca bitir.

Tum dogal sayılar 1'e ve kendisine bolunebildiği için;
Çarpanları bulan donguden bu değerleri arama.
"""

"""

import sys

tri, count, tmp, target = 1, 0, 2, 16

while True:
    count = count + 1
    tri = int((count * (count + 1))/2)

    for i in range(2,tri):

        if tri % i == 0:
            tmp = tmp + 1
            print("tri= "+str(tri)+" i= "+str(i)+" tmp= "+str(tmp))

            if tmp > target:
                print(tri)
                sys.exit()

        if tri % 2 == 0 and i == tri/2:
            #print(i)
            break
        elif tri % 2 == 1 and i == tri/3:
            #print(i)
            break

    tmp = 2

"""

"""
Method: 2

Örnek olarak 28 üçgensel sayısı için:

28 = 1, 2, 4, 7, 14, 28 -> 1x28, 2x14, 4x7, 7x4, 14x2, 28x1

15 üçgensel sayısı için:

15 = 1, 3, 5, 15 -> 1x15, 3x5, 5x3, 15x1


Yani her üçgensel sayının çarpanları kendini 2 kez tekrarlıyor.
Bu yüzden çarpanları bulan döngüde sayının karakökü kadar döndürüp;
Her bulduğumuz çarpan için 2 tane bulduk diyebiliriz.

Karakökü alınabilen sayıların çarpanlarında
bir sayıdan sadece bir çarpan üretilebilir.

Her bulduğumuz sayıya 2 eklediğimiz için sayının karesi alınabiliyorsa;
Çarpan sayısından bir çıkartıyoruz.

Örnek olarak 36'nın karesi 6, 6'nın normalde 2 kere kullanılması lazımdı
ama karesi alınabilir olduğu için 6'lı çarpan sayısı sadece 1 adet.

36 = 1, 2, 3, 6, 4, 9, 12, 18, 36 ->
1x36, 2x18, 3x12, 4x9, 6x6, 9x4, 12x3, 18x2, 36x1

"""

import time
start = time.time()

count, num = 0, 0
target = 500  # min target + 1 degeri kadar böleni olan ilk doğal sayı


def get_triangle_number(n):
    tri = int((n * (n + 1)) / 2)
    return tri


def divisors(n):
    tmp = 0
    for i in range(1, int(num**0.5)):
        if n % i == 0:
            tmp = tmp + 2
        if i * i == n:
            tmp = tmp - 1

    return tmp


while True:
    count = count + 1
    num = get_triangle_number(count)
    if divisors(num) > target:
        print(num)
        break


elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds")

# 10.15684175491333 seconds
