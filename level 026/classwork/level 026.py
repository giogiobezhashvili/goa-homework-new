
# 1
numbers = [10, 20, 30, 40, 50]

snum = 0

for num in numbers:
    snum += num

ag = snum / 5


print(snum)
print(ag)

# 2
while True:
    user_number = int(input("შეიყვანე რიცხვი: "))

    if user_number != 5:
        print("არასწორია, სცადე თავიდან")
        continue  
    else:
        print("გილოცავ! სწორად გამოიცანი")
        break  

# 3
while True:
    number = int(input("შეიყვანე რიცხვი: "))

    if number % 2 != 0:
        print("ეს კენტია, სცადე თავიდან")
        continue 
    else:
        print("ეს ლუწი რიცხვია")
        break  








