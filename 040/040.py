"""

While döngüsü kurup kontrol ifadesi koyabilirdim ancak her seferinde
kontrol ifadesi programı ~2 kat yavaşlatacaktır.
Bu yüzden aşağıdaki hesabı yaptım.

(9 * 1) + (99 * 2) + (999 * 3) +
(9999 * 4) + (99999 * 5) + (76135 * 6) = 1000005

Yani döngü toplamda 9 + 99 + 999 + 9999 + 99999 + 76135 kez döndüğünde
1000005 basamak üretiyor.

"""

import time
start = time.time()

num = ""

# Basamakları oluştur
for i in range(1, 9 + 99 + 999 + 9999 + 99999 + 76135 + 1):
    num = num + str(i)

# Sonucu yazdır
print(int(num[0]) * int(num[9]) * int(num[99]) * int(num[999]) *
      int(num[9999]) * int(num[99999]) * int(num[999999]))

elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds")

# This code took: 0.09795546531677246 seconds
