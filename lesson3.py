 # lesson 5
# 05.12.2023
# String (unicode-table.com)

#name = "sardorbek"
#surname = "nasrullayev"
#print(f"{name} {surname}")
#print(f"Hello, my name is {name}. \tMy surname is {surname}.")

# Method
#full_name = f"{name} {surname}"
#print(full_name.upper())
# Matnni katta harflarda chiqarish
#print(full_name.lower())
# Matnni kichik harflarda chiqarish
#print(full_name.title())
# Matndagi so'zlarni birinchi harfini katta harflarda chiqarish
#print(full_name.capitalize())
# Matndagi birinchi so'zni birinchi harfini katta harfda chiqarish

#fruit = "   apple   "
#print("I like " + fruit.lstrip() + ".")
# Chap tomondagi bo'shliqlarni matindan olib tashlaydi
#print("I like " + fruit.rstrip() + ".")
# O'ng tomondagi bo'shliqlarni matindan olib tashlaydi
#print("I like " + fruit.strip() + ".")
# Bo'shliqlarni matindan olib tashlaydi

# Input() function
#city = input("Enter the your city: \n")
#print(city.title() + " is very beautiful.")

# Homework
# 1-mashq
#kocha = "Bog'bon"
#mahalla = "Sog'bon"
#tuman = "Bodomzor"
#viloyat = "Samarqand"
#print(kocha+" ko'chasi, "+mahalla+" mahallasi, "+tuman+" tumani, "+viloyat+" viloyati.")

# 2-mashq
kocha = input("Ko'cha nomini kiriting: ")
mahalla = input("Mahalla nomini kiriting: ")
tuman = input("Tuman nomini kiriting: ")
viloyat = input("Viloyat nomini kiriting: ")
# print(kocha+" ko'chasi, "+mahalla+" mahallasi, "+tuman+" tumani, "+viloyat+" viloyati.")

# 3-mashq
# print(kocha+" ko'chasi,\n"+mahalla+" mahallasi,\n"+tuman+" tumani,\n"+viloyat+" viloyati.")

# 4-mashq
manzil = f"{viloyat} viloyati {tuman} tumani {mahalla} mahallasi {kocha} ko'chasi."
# print(manzil)

# 5-mashq
print(manzil.title()) # stringdagi barcha so'zlarni bosh harfini kattada yozadi
print(manzil.upper()) # Barcha harflarni kattada yozadi
print(manzil.lower()) # Barcha harflarni kichkinada yozadi
print(manzil.capitalize()) # Birinchi so'zni bosh harfini kattada yozadi
# lstrip() — matn boshidagi bo'shliqni,
# rstrip() – matn oxiridagi bo'shliqni,
# strip() — matn boshi va oxiridagi bo'shliqlarni olib tashlaydi