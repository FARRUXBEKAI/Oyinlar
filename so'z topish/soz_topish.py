# 03/03/2022

# Python asoslari

# Mavzu: "So'z topish " o'yinini yasash

# Muallif: Farrux Sotivoldiyev

import random 
from lotin import sozlar

def soz_tanla():
    soz = random.choice(sozlar)
    while '-' in soz or ' ' in soz or "ʻ" in soz:
        soz = random.choice(sozlar)
    return soz.lower()

def solishtir(foydalanuvchi,soz):
    solishtirgin = ""
    for harf in soz:
        if harf in foydalanuvchi.lower():
            solishtirgin += harf
        else:
            solishtirgin += "-"
    return solishtirgin

def oyin():
    soz = soz_tanla()
    sozdagi_harflar = set(soz)
    foydalanuvchi_harflari = ''
    print(f"Men {len(soz)} ta harfdan iborat so'z o'yladim.Topa olasizmi?")

    while len(sozdagi_harflar) > 0:
        print(solishtir(foydalanuvchi_harflari,soz))
        if len(foydalanuvchi_harflari) > 0:
            print(f"Shu vaqtgacha kiritgan harflaringiz: {foydalanuvchi_harflari}")

        foydalanuvchi = input("Xarf kiriting: ").lower()
        if foydalanuvchi in foydalanuvchi_harflari:
            print("Avval bu harfni kiritgansiz.Boshqa harf kiriting: ")
            continue
        elif foydalanuvchi in soz:
            sozdagi_harflar.remove(foydalanuvchi)
            print(f"{foydalanuvchi} harfi tog'ri")
        else:
            print("Bunday harf yo'q!")
        foydalanuvchi_harflari += foydalanuvchi
    print(f"Tabriklaymiz {soz} so'zini {len(foydalanuvchi_harflari)} ta urunishda topdingiz")

oyin()