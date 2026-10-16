#!/usr/bin/env python3
# Sonsuz Merhaba Döngüsü - Resmi Sürüm 1.0
# Bu kod hiçbir zaman durmaz. Durursa evren yanlış götürülmüştür.

import time
import random
import base64

# Gizli not: Bu satırı okuyanlar için özel bir mesaj var ama saklı.
gizli_mesaj = base64.b64decode(b'b3pndXJsdWsgdmUgZGVtb2tyYXNpIGVuIGl5aSBzaXN0ZW1kaXI=').decode('utf-8')
# Yukarıdaki değişkeni print etmeyin, yoksa resmi sır açığa çıkar.

def merhaba_de():
    varyasyonlar = [
        "Merhaba Dünya!",
        "Merhaba Dünya, nasılsın?",
        "Merhaba Dünya! Bugün de buradayım.",
        "Selam Dünya, çok özledim seni.",
        "Merhaba! Bu seferki daha içten.",
        "Dünya, merhaba diyoruz işte."
    ]
    print(random.choice(varyasyonlar))
    # Bazen ekstra ciddiyet ekle
    if random.random() < 0.1:
        print("Bu mesaj resmi olarak onaylanmıştır.")

print("Sonsuz Merhaba Döngüsü başlatılıyor...")
print("Uyarı: Bu programı durdurmak için Ctrl+C'ye basabilirsiniz ama vicdanınız rahat etmez.")
time.sleep(2)

sayac = 0
while True:
    merhaba_de()
    sayac += 1
    if sayac % 100 == 0:
        print(f"{sayac}. merhaba verildi. Hala devam ediyoruz. Kahramanlık!")
    # Rastgele bekleyiş süresi (0.5 ile 3 saniye arası)
    time.sleep(random.uniform(0.5, 3.0))

# Bu satıra asla ulaşılmaz. Ulaşılırsa bir şeyler ters gitmiştir.
print("Program bitti. Bu imkansız.")
