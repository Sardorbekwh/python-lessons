# lesson 10 
# 21.12.2023
# If - else

#   homework
# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat 
# tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga 
# chqaring. GM uchun ikkala harfni katta qiling.
"""
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car=="gm":
        print(car.upper()) # upper methodi
    else:
        print(car.title()) # title methodi
"""

# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
"""
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car!="gm":
        print(car.title()) # title methodi
    else:
        print(car.upper()) # upper methodi
"""

# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, 
# "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" 
# xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" 
# matnini konsolga chiqaring.
"""
login = input("Loginni kiritng: ")
login.lower()
if login == "admin":
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    login.upper()
    print(f"Xush kelibsiz, {login}!")
"""

# Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng 
# bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
"""
f_number = int(input("1-sonni kiriting: "))
s_number = int(input("2-sonni kiriting: "))
if f_number == s_number:
    print("Sonlar teng")
else:
    print("Sonlar teng emas")
"""

# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga 
# "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 
"""
number = int(input("Son kiring: "))
if number>0:
    print(f"{number} musbat son")
else:    
    print(f"{number} manfiy son")
"""

# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini 
# hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan 
# xabarni chiqaring. 

import math
son = int(input("Son kiriting: "))
if son>0:
    javob = math.sqrt(son) # function
    print(int(javob))









