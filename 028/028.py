"""

Bize 1001x1001 lik bir sayı kümesi oluşturmamız söylenmiş.
İlk değeri çıkartıp kümeyi ikiye bölersek 500 adet halka'ya ihtiyacımız var.
Her halka 8'in katı.
Her halkada atlama değeri 2 artıyor, 2, 4, 6..

"""

import time
start = time.time()

# Zinciri 1 değeri ile başlat
num = 1

# Sayı deposu
dump = []
tmp = []

# Halka arası atlama değeri
jump = 0

# Köşe sayıların toplamı
sum = 0

# Sayıları oluştur
for i in range(1, 501):  # toplam 1001 x 1001 diyor yani 500 adet halka var
    for j in range(i * 8):
        num = num + 1
        tmp.append(num)

    dump.append(tmp)
    tmp = []

# Tüm halkaları döndür
for i in dump:
    # Atlama sırasını ayarla
    jump = jump + 2
    # Halkanın elemanlarını döndür
    for j in i:
        if j % jump == 0:
            sum = sum + j + 1

# İlk değeri toplama katarak yazdır
print(sum + 1)

elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds")

# This code took: 0.25845885276794434 seconds
