from time import time,sleep
from random import randint,randrange
from sekundomer import sekundomer

print("Assalomu alaykum 'Brain up' o'yinimizga xush kelibsiz")
print("""O'yin shartlari:
1.10 ta misol beriladi
2.Har bir savol uchun 10 sekund vaqt """)
input("O'yinni boshlash uchun hohlagan tugmangizni bosing")
while True:
    javoblar = []
    korsatgich = 0
    for k in range(1, 11):
        son1 = randint(1,10)
        son2 = randint(2,8)
        son3 = randrange(4,50,4)
        son4 = randrange(2,5,2)
        son5 = randint(4,10)

        t1 = time()
        javob = float(input(f"{k} - savol\n{son1} * {son2} - {son3} / {son4} + {son5}\n>>> "))
        t2 = time()
        t = t2 - t1

        if javob == son1 * son2 - son3 / son4 + son5 and t <= 10:
            natija = "To'g'ri 😊"
            korsatgich += 1
        else:
            natija = "Xato 😔"
        javoblar.append(f"{k}-savol: {natija} vaqt = {round(t)} sekund")
    
    for javob in javoblar:
        print(javob)
    
    print(f"Ko'rsatgich: {korsatgich*10} %")
    
    savol = input("Yana o'ynaysizmi? ha/yoq >>>")
    print("3 sekunddan so'ng o'yin boshlanadi...")
    sekundomer(3)
    if savol == 'yoq':
        print("O'yin tugadi😊")
        break