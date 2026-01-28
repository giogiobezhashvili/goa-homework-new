# 1

numbers = [1, 2, 3, 4, 5]
print(len(numbers)) 


# 2

names = ["Giorgi", "Nika", "Luka", "Saba", "Ana"]

user_name = input("შეიყვანე სახელი: ")
names.append(user_name)  

print(names)


# 3

names.insert(3, "Tarieli")
print(names)

# 4

names.pop(4)
print(names)


# 5
names.remove("Nika")  
print(names)

# 6

search_name = input("შეიყვანე სახელი მოსაძებნად: ")

if search_name in names:
    print(names.index(search_name))
else:
    print("not index in list")


# 7


numbers = [10, 20, 30, 40, 50]

for i in range(5):
    num = int(input("შეიყვანე რიცხვი: "))
    numbers.append(num)

print(numbers)
















