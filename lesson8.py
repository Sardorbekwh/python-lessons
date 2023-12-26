# lesson 11
# 23.12.2023
# Bir nechta shartlarni tekshirish 
# if - elif - else

# homework
# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son 
# kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
"""
j_son = int(input("Juft son kiritng: "))
if j_son%2==0:
    print("Rahmat!")
elif j_son%2!=0:
    print("Bu son juft emas")
"""
 
# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini
# quyidagicha chiqaring:
# 1. Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# 2. Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# 3. Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
"""
yosh = int(input("Yoshingiz nechida? "))
if yosh<4 or yosh>60:
    print("Sizga chipta bepul")
elif yosh<18:
    print("Sizga chipta 18000 so'm")
elif yosh>18:
    print("Sizga chipta 20000 so'm")
""" 

# Foydalanuvchidan ikkita son kiritishni so'rang, sonlarni solishtiring va 
# ularning teng yoki katta/kichikligi haqida xabarni chiqaring
"""
son1 = input("1-sonni kiriting: ") 
son2 = input("2-sonni kiriting: ") 
if son1==son2:
    print("Sonlar teng")
elif son1>son2:
    print(f"{son1} katta {son2} dan")
else:
    print(f"{son2} katta {son1} dan")
"""

# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. 
# Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 
# 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati
# bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" 
# aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
"""
mahsulotlar = ['un', 'non', 'tuz', 'nok', "saryog'", 'cola', "yog'", 'tut', 'suv', 'fanta']
savat = []
#savat = input("5 ta mahsulot kiriting: ")
for soni in range(5):
    savat.append(input(f"{soni+1}-mahsulotni kiriting: "))
if savat:
    for buyurtma in savat:
        if buyurtma in mahsulotlar:
            print(f"{buyurtma} do'konimizda bor")
        else:
            print(f"{buyurtma} do'konimizda yo'q")        
else:
    print("Savat bo'sh")
"""

# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot 
# kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, 
# bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas 
# degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan
# barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi 
# mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
"""
mahsulotlar = ['un', 'osh', 'non', 'choy', 'suv', 'limon', 'gul', 'mum', 'fanta']
b_mahsulotlar = []
y_mahsulotlar = []
buyurtma = []
for son in range(5):
    buyurtma.append(input(f"{son+1}-mahsulotni kiriting: "))
if buyurtma:    
    for saralash in buyurtma:
        if saralash.strip().lower() in mahsulotlar:
            b_mahsulotlar.append(saralash)
        else:
            y_mahsulotlar.append(saralash)
else:
    print("Sizning savatingiz bo'sh")
if y_mahsulotlar:
    print("Quydagi mahsulotlar do'konimizda yo'q: ")
    for y in y_mahsulotlar:
        print(y_mahsulotlar)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
"""

# Foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
# Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan 
# loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar 
# ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks 
# holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.   
"""
users =['sardorbek', 'sanjarvek', 'tohirbek', 'murod', 'bahodir', 'abror']
login = input("Yangi login tanlang: ")
if login.strip().lower() not in users:
    print("Login band, yangi login tanlang!")
else:
    print("Xush kelibsiz, foydalanuvchi!")
"""

# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan 
# sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga 
# chiqaring.

son = int(input("Istalgan butun son kiritng: "))
for b in range(2,11):
    if son%b==0:
        print(f"{son} soni {b} ga qoldiqsiz bo'linadi.")
        






















 










































