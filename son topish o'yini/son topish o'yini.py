#!/usr/bin/env python
# coding: utf-8

# # 20/12/2021
# 
# # Python asoslari
# 
# # Mavzu: Son topish  o'yinini yasash
# 
# # Muallif: Farrux Sotivoldiyev
# 

# In[1]:


#son topish o'yini
from random import randint
while True:
    def sontop_man(x=10):
        tasodifiy_son = randint(1, x)
        print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi ?")
        urunish = 1
        while True:
            taxmin = int(input(">>>"))
            if taxmin < tasodifiy_son:
                print("Xato.Men o'ylagan son bundan kattaroq.Yana harakat qiling: ")
            elif taxmin > tasodifiy_son:
                print("Xato.Men o'ylagan son bundan kichikroq.Yana harakat qiling: ")
            else:
                break
            urunish += 1
        print("-----------------------------")
        print(f"Tabriklaymiz.Siz {urunish} ta urnishda topdingiz ")
        return urunish


    def sontop_pc(x=10):
        print("-----------------------------")
        input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing.Men topaman!")
        quyi = 1
        yuqori = x
        urunish_pc = 1
        while True:
            if quyi != yuqori:
                taxmin = randint(quyi, yuqori)
            else:
                taxmin = quyi
            javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                          f"men o'ylagan son bundan kattaroq (+) yoki kichikroq (-) >>>".lower())
            if javob == '-':
                yuqori = taxmin - 1
            elif javob == '+':
                quyi = taxmin + 1
            else:
                break
            urunish_pc += 1
        print("-----------------------------")
        print(f"Topdim! {urunish_pc} ta urunishda")
        return urunish_pc


    x = randint(1, 100)

    y = sontop_man(x)
    z = sontop_pc(x)


    if y == z:
        print("-----------------------------")
        print(f"Durrang.Ikkimiz ham {y} ta urunishda topdik😬")
        tanlov = input(f"Yana o'ynashni hohlaysizmi? ha/yoq")
        if tanlov=="yoq":
            break
    if y < z:
        print("-----------------------------")
        print(f"Siz yutdingiz😞.Siz {y} ta urunishda,men esa {z} ta urunishda topdimm")
        tanlov = input(f"Yana o'ynashni hohlaysizmi? ha/yoq")
        if tanlov=="yoq":
            break
    if y > z:
        print("-----------------------------")
        print(f"Siz yutqazdingiz😊.Men {z} ta urunishda,siz esa {y} ta urunishda topdingiz")
        tanlov = input(f"Yana o'ynashni hohlaysizmi? ha/yoq")
        if tanlov=="yoq":
            break
print("O'yin tugadi😊")

