

name = input("შეიყვანეთ სახელი: ")
print(name.upper())

print("_______2_______")

name = input("შეიყვანეთ სახელი: ")
print(name.lower())

print("_______3_______")


name = input("შეიყვანეთ სახელი: ")
print(name.capitalize())


print("_______4_______")

word = "python"
symbol = input("შეიყვანეთ სიმბოლო: ")

if symbol in word:
    print(f"{symbol} - {word.index(symbol)}")
else:
    print("This symbol is not in word")




print("_______5_______")


my_name = "Giorgi"
print(len(my_name))


print("_______6_______")




name = input("შეიყვანეთ სახელი: ")

if name.lower().startswith("g"):
    print("სახელი იწყება ასო 'g'-თი")
else:
    print("სახელი არ იწყება ასო 'g'-თი")



print("_______7_______")


name = input("შეიყვანეთ სახელი: ")

if name.lower().endswith("l"):
    print("სახელი მთავრდება ასო 'l'-თი")
else:
    print("სახელი არ მთავრდება ასო 'l'-თი")

























