"""

Geliştirici Notları

Toplam 16384 rota olduğu verilmiş, bunun anlamı 2**14 + 1 kadar rota var.
Neden +1? 00000000000000 rotası da var çünkü.
Binary ile kolay bir şekilde benzersiz rotalar oluşturmak mümkün.
2'lik tabanda 0 sayısına 16384'kez 1 eklersek sonuç 11111111111111 olur.
Gördüğü üzere 14 basamak var, bizde rota çizerken 14 basamak kullanıyoruz.
15. basamak etkisiz olduğu için sonucumuza ekleyip yazdırıyoruz.

Her rotaya tek tek baktığımız için brute force yöntemi kullanmış oluyoruz.

"""

import time
start = time.time()

dummy = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

# Dummy verilerini bir listeye dönüştür
dummy = list(map(int, dummy.split()))

# Çok boyutlu bir liste oluşturmak için gerekli değişkenler
nums = []
tmp_list = []
counter = 0

# Çok boyutlu bir liste oluştur

# Üçgenin tüm satırlarını dön (15 satır)
for i in range(1, 16):  # 1 - 15

    # Satırdaki tüm elemanları dön
    for j in range(i):
        tmp_list.append(dummy[counter])
        counter = counter + 1

    nums.append(tmp_list)
    tmp_list = []


# Bulunan maximum sayı ve rota toplamı için gerekli değişkenler
max, route_sum = 0, 0

# Rota üretiminde kullanılacak değişkenler
route = "0"
route_filled = ""


# Sum binary numbers, returns a string
def bin_add(*args):
    return bin(sum(int(x, 2) for x in args))[2:]


# 2**14 adet rota var
# 11111111111111 toplam 16383 yapıyor. +1 ise 00000000000000 rotası

# Rota üret
for i in range(16384 - 1):
    route = bin_add(route, "1")

    # 8192 sayının başında basamağı 14'e tamamlayacak şekilde sıfır ekleniyor
    if len(route) <= 14:
        route_filled = '00000000000000'[:-len(route)] + route

    # Satır içindeki pozisyonumuz
    pos = 0

    # Rotanın toplamı hesaplanıyor
    for i, letter in enumerate(route):
        if int(letter) == 1:
            pos = pos + 1
        elif int(letter) != 0:
            pos = pos - 1

        route_sum = route_sum + nums[i + 1][pos]

    if route_sum > max:
        max = route_sum

    route_sum = 0

# Tepedeki sayıyı rotaya ekleyerek yazdır
print(max + 75)

elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds")

# This code took: 0.16301679611206055 seconds
