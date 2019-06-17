"""
# Buradaki algoritmanın adı Trial Division
# Yazması ve anlaması çok kolay ancak çalışma hızı berbat^1000
# Muhtemelen cevabı bulmak saatler hatta günler sürer

num = 2000000
sum = 0
prime = False

for i in range(3,num,2):

    for j in range(3,i):
        if i % j == 0:
            prime = False
            break
        else:
            prime = True

    if prime:
        sum = sum + i

print(sum+2+3) # 2 ve 3 asal oldugu halde donguye girmedigi icin eklendi
"""

"""
# Erotosten Kalburu adlı bir algoritma kullandım
# Kısaca asal sayıların katlarını bir listeden eleyerek listeyi daraltıyoruz
# Karmaşık ama daha hızlı bir algoritma daha varmış: Atkin Kalburu

+ 2000000 elemanlı, tüm elemanları true olan bir liste oluştur
+ 2 den başlayıp 2000000 kez dönen bir döngü oluştur
+ Eğer liste[i] true ise i elemanı asal bir sayıdır, topla
+ Sonrasında asal sayının katlarını liste üstünde false'a çevir
"""

import time
start = time.time()

num = 2000000
list = [True] * num
sum = 0

for i in range(2, num):
    if list[i]:
        sum = sum + i
        for j in range(i * i, num, i):
            list[j] = False

print(sum)

elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds")

# 0.6831727027893066 seconds
