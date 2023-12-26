# lesson 7
# 06.12.2023
# Lists

"""
fruits = ["apple", "orange", "banana", "limon"]
numbers = [23, 63, 3.54, -78.2, 88829, 100]
thinks = ["book", 43, "notebook", 4.4]
empty = []
"""


"""
print(fruits[1])
print(fruits[-1])
print(fruits[-1].title())
print(numbers[0]+numbers[-1])
fruits[0] = "nack" 
print(fruits)
fruits.append("watermelon") 
# add the elements to list
print(fruits)
# append method - add the items
fruits.insert(0, "melon")
print(fruits)
# insert method - add item by index 
"""

"""
cars = []
cars.append("tiko")
print(cars)
cars.append("malibu")
cars.append("damas")
cars.append("cobalt")
print(cars)
"""

#cars = ["t", "k", "h", "u"] 
# tuples write the ()
# list wirite the []
#del cars[2]
#print(cars)

"""
cars.insert(0, "damas")
print(cars)
cars.append("damas")
print(cars)
cars.remove("damas")
# remove methode - 
print(cars)
"""

"""
prodacts = ["milk", "orange", "spoon", "phone"]
prodact = prodacts.pop(2)
print("I buy "+prodact+".")
print("Unbought prodacts: ", prodacts)
prodact2 = prodacts.pop()
# pop method - pop the element from list and put to the value
print(prodacts)
"""

# homework
# 1-mashq
"""
name = ["Tohir", "Murod", "Bahodir", "Muzaffar", "Abror"]
print("Assalomu alaykum " +name[0]+ " Are you ok? Can you tell me where is "+name[1]+"?" )
print("Please ask from "+name[2]+".")
"""

# 2-mashq
"""
numbers = [2, 4.2, -6, 11]
numbers.append(2)
print(numbers)
numbers.insert(-1, 8)
print(numbers)
del numbers[-1]
print(numbers)
numbers.remove(2)
print(numbers)
numbers[0] = 3
print(numbers)
"""

# 3-mashq
"""
historical_persons = ["Ibin Sino", "Alisher Navoiy", "Tomis Edison"]
moderin_persons = ["Anvar Narzullayev", "Ilon Mask", "Benidick Kembrpich"]
print("I wont conversetion from historical persons with "+ historical_persons[2]+",")
print("from modern persons "+moderin_persons[0]+".")
"""

# 4-mashq
"""
friends = []
friends.append("Murod")
friends.append("Bahodir")
friends.append("Tohir")
friends.append("Jasur")
friends.append("Zafar")
friends.append("Abror")
print(friends)
friends.remove("Murod")
friends.remove("Abror")
print(friends)
friends.insert(0, "Kamron")
friends.insert(-1, "Javohir")
friends.insert(4, "Elbek")
print(friends)
gost_1 = friends.pop(0)
gost_2 = friends.pop(3)
print(friends)
gosts = []
gosts.append(gost_1)
gosts.append(gost_2)
print(gosts)
"""

# lesson 8
# 07.12.2023
# Lists


#cars = ['cobalt', "bmw", "mers", 'wolks wagen', 'kia']
#cars.sort()
#print(cars)
"""
# sort method - sorted in list (a, b, ... y, z)
#cars.insert(1, "BMW")
# sort method first write capital laters
#cars.sort()
#print(cars)
#print(sorted(cars))
# sorted method - sorted in list but don't change from the memory (database)
#cars.sort(reverse=True)
# Reverse atribute of the sort method - change the list (z, y, w ... c, b, a) 
#print(cars)
print(sorted(cars, reverse=True)) # This is same with the up row

numbers = [23, 9.9, 12, -2, 38, 3, 999, -5]
print(sorted(numbers, reverse=True))
numbers.reverse()
print(numbers)
"""

"""
#numbers = [32, 9, 0, -3, 99, 6, 8.3, 19,2, -9, 91]
#print(len(numbers))
# len method - size of list
#numbers = list(range(0,10))
#print(numbers)
#odd_numbers = list(range(1,10,2))
# third value is steps (1, 3, 5,.. 77, 79, 81)
#print(odd_numbers)
#max_number = max(numbers)
# Find the max number from list 
#print(max_number)
#min_number = min(numbers)
#print(min_number)
prices = [23000, 10000, 4000, 8000, 25000, 9000]
sum_prices = sum(prices)
print(sum_prices)
print(prices[:3])
print(prices[1:4])
print(prices[3:])
cars = ['bmw', 'tico', 'mercedes', 'lexus', 'tesla']
my_cars = cars[:] # copy the elements
"""

# Tuples 
# 07.12.2023
 
""" 
toys = ('spider', 'robot', 'car', 'water weapon')
# tuples don't change but it is possible
toys = list(toys)
print(type(toys))
print(toys)
toys.append("doll")
print(toys)
# tuples change the list so can add the element
toys = tuple(toys)
print(type(toys))
print(toys) 
# list change the tuples 
"""

# homework
# 15.12.2023

"""
davlatlar = {"Uzb", "USA", "UK", "RU", "TJ"}
print(davlatlar)
# listni uzunligini konsulga chiqaring
print(len(davlatlar))
# listni to'g'ri tartiblang
print(sorted(davlatlar))
# listni teskari tartiblang
print(sorted(davlatlar, reverse=True))
# asil ro'yxatni konsulga chiqaring
print(davlatlar)
# ro'yxatni reverse() methodi orqali teskari chiqaring
davlatlar.reverse()
print(davlatlar)
"""
#sort methodi yordamida ro'yxatni avval alifbo tartibida keyin esa alifboga teskari tarribda chiqaring
#shaharlar = {'Guliston', 'Buxoro', 'Samarqand', 'Andijon'}
#shaharlar.sort()
#shaharlar.sort(reverse=True)
#print(shaharlar)

# 120 dan 1200 gacha juft sonlarni chiqaring
#numbers = list(range(120,1200,2))
#print(numbers)

# shu sonlarning yig'indisini hisoblang
#all_sum = sum(numbers)
#print(all_sum)

# ro'yxatdan eng katta va eng kichik raqamlar ayirmasini hisoblang
#min_number = min(numbers)
#max_number = max(numbers)
#substraction = max_number-min_number
#print(substraction)

# ro'yxatdagi elementlar sonini hisoblang
#print(len(numbers))

# ro'yxat boshidan, oxiridan, o'rtasidan 20 ta sonni konsulga chiqaring
#print(numbers[0:20])
#print(numbers[-20:])
#print(numbers[530:550])

#taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['osh','somsa','norin','shashlik','qozonkabob']

#nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]

#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove('norin')
nonushta.remove('shashlik')
nonushta.remove('qozonkabob')
nonushta.append('non va qaymoq')
nonushta.append('issiq non')

#Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(taomlar)
print(nonushta)

#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
nonushta[0] = "qaymoq va non"
