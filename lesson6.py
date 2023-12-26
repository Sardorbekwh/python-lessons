# lesson 9
#21.12.2023
# For loop

#homework
#Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi 
#har bir ismga takrorlanuvchi xabar yozing
"""
ismlar = ["Tohir", "Jasur", "Abror", "Odil", "Samandar","Javohir"]
n=0
for ism in ismlar:
    print(f"Assalomu alaykum {ism}")
    n+=1
"""
#Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" 
#degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
#print(f"Kod {n} martta takrorlandi.")

#10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir 
#elementining kubini yangi qatordan konsolga chiqaring.
"""
sonlar = list(range(11,100,2))
for toq_son in sonlar:
    print(f"{toq_son} ning kubi {toq_son**3} ga teng.\n")
"""

#Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar
#degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
"""
kinolar = []
print("Yoqtirgan 5 ta kinolar nomini kiritng")
for soni in range(5):
    kinolar.append(input(f"{soni+1}-kino nomini kiriting: "))
print(kinolar)
"""

#Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) 
#so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga 
#yozing. Ro'yxatni konsolga chiqaring.

odamlar = []
n = int(input("Bugun nechta odam bilan suhbatlashdingiz: "))
for soni in range(n):
    odamlar.append(input(f"{soni+1}-odamni ismini kiritng: "))
print(odamlar)