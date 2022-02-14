# Quduq, Qaychi, Qog'oz o'yini

from random import randint

while True:
    print("Assalomu alaykum!\n<<< Quduq, Qaychi, Qog'oz >>> o'yiniga xush kelibsiz!")
    print("""
    1.Quduq
    2.Qaychi
    3.Qogoz
    ⛔-> #

    Bulardan birini yozing ...
    """)

    sizda = input("::::")
    siz = sizda.title()
    shart = randint(0,2)
    shartcha = ['Quduq','Qaychi',"Qogoz"]
    kompyuter = shartcha[shart]
    if siz == '#':
        print("Qale chiqibdi 😉")
        break
    elif (siz == 'Quduq' ) and (kompyuter == 'Qaychi'):
        print(f"<<< Siz yutdingiz🙂! >>> Kompyuter {kompyuter}ni tanlagan edi...") 

    elif (siz == 'Quduq' ) and (kompyuter == "Qogoz"):
        print(f"<<< Siz yutqazdingiz😞! >>> Kompyuter {kompyuter}ni tanlagan edi...")

    elif (siz == 'Qaychi') and (kompyuter == 'Quduq'):
        print(f"<<< Siz yutqazdingiz😞! >>> Kompyuter {kompyuter}ni tanlagan edi...")

    elif (siz == 'Qaychi') and (kompyuter == "Qogoz"):
        print(f"<<< Siz yutdingiz🙂! >>> Kompyuter {kompyuter}ni tanlagan edi...")

    elif (siz == "Qogoz") and (kompyuter == "Qaychi"):
        print(f"<<< Siz yutqazdingiz😞! >>> Kompyuter {kompyuter}ni tanlagan edi...")

    elif (siz == "Qogoz") and (kompyuter == "Quduq"):
        print(f"<<< Siz yutdingiz🙂! >>> Kompyuter {kompyuter}ni tanlagan edi...")

    elif siz == kompyuter:
        print("Durrang🤔!")
    else:
        print("Hech narsa yozmadingiz yoki boshqa narsa yozdingiz!")
        print("Boshqattan tanlang...")

print("O'yin tugadi!")



