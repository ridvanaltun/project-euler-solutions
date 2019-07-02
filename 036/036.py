"""

Virgüllü bir sayıyı integer'a çevirince virgül kısmı siliniyor,
algoritmada cut değişkenini bu özellik ile ayarladım.

"""

import time
start = time.time()

sum = 0

for num in range(1000001):  # 0 - 1000000

    binary = bin(num)[2:]
    first_part = ""
    second_part = ""

    # Decimal kontrol için cut değişkenini ayarla
    cut = int(len(str(num)) / 2)

    # Decimal palindrome mu? Veri oluştur.
    if len(str(num)) % 2 == 0:
        first_part = str(num)[:cut]  # bas kısım
        second_part = str(num)[cut:][::-1]  # son kısım
    else:
        first_part = str(num)[:cut]
        second_part = str(num)[cut + 1:][::-1]

    # Decimal palindrome ise binary palindrome kontrol et
    if first_part == second_part:
        cut = int(len(binary) / 2)

        if len(binary) % 2 == 0:
            first_part = binary[:cut]
            second_part = binary[cut:][::-1]
        else:
            first_part = binary[:cut]
            second_part = binary[cut + 1:][::-1]

        if first_part == second_part:
            sum = sum + num

    else:
        pass

print(sum)

elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds")

# This code took: 1.9870305061340332 seconds
