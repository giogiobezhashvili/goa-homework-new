
# 1

num = 12

if num > 10:
    print("more than 10")
else:
    print("less than 10")


# 2

num = int(input("შემოიტანე რიცხვი:"))

if num == 15:
    print("equal to 15")
else:
    print("not eqtuali to 15")

# 3 

an = input("შემოიყვანე ჯგუფი")

if an == "grop84":
    print("you are correct")
else:
    print("yoou are wrong")

# 4


for i in range(50,100,5):
    print(i)

# 5



for i in range(13):
    print("giorgi bezhashvili")

# 6
num=20

while num <= 50:
    print(num)
    num += 1


# 7


for i in range(100):
    print(i)


num = 0

while num <= 100:
    print(num)
    num += 1


# 8

for i in range(101):
    print(i)


i = 0
while i <= 100:
    print(i)
    i += 1

# 9


for i in range(10,20):
    print(i)

num = 10

while num <= 20:
    print(num)
    num += 1



# 10

for i in range(100,201,5):
    print(i)

num = 100

while num <= 200:
    print(num)
    num += 5

# 11


for i in range(10,-1,-1):
    print(i)

num = 10

while num >= 0:
    print(num)
    num -=1 

# 12

num = float(input ("შემოიყანე ნებისმიერ რიცხვი:"))

if num > 0:
    print("შენი რიცხვი დადებითია")
elif num < 0 :
    print("შენი რიცხვი უარყფითია")
else:
    print("შენი რიცხვი ნულია ")

# 13


age = int(input("შემოიყვანეთ თქვენი ასაკი:"))


if age < 0:
    print("არასწორი ინფორმაცია")

elif age < 12:
    print("შენ ბავშვი ხარ")
elif age < 19:
    print(" შენ მოზარდი ხარ")
elif age < 64:
    print("ზრდასრული ადამიან ხარ")
elif age < 120:
    print("ხანში შესული ადამიანი  ხარ")
else:
    print("გურუ ან ჯადოქარი ხარ")


# 14


a = float(input("შეიყვანე პირველი რიცხვი:"))
b = float(input("შეიყვანე მეორე რიცხვი:"))
c = float(input("შეიყვანე მესამე რიცხვი:"))

print(max(a,b,c))


# 15

data = int(input("შემოიყვანე რიცხვი 1-დან 7-ის ჩათვლით:"))

if data == 1:
    print("ორშაბათი")
elif data == 2:
    print("სამშაბათი")
elif data == 3:
    print("ოთხშაბათი")
elif data == 4:
    print("ხუთშაბათი")
elif data == 5:
    print("პარასკევი")
elif data == 6:
    print("შაბათი")
elif data == 7:
    print("კვირა")
else:
    print("არ ვიცი ეგ რა დღეა")



# 16


num = int(input("შემოიყვანე რიცხვი:"))

if num > 50:
    print(num * 5)
else:
    print(num ** 2)

# 17

password = input("შეიყვანე პარპლი: ")

if password == "gio123":
    print("Password is correct!")
else:
    print("Incorrect password!")



# 18

n = int(input("შემოიტანე რიცხვი: "))

total = 0
for i in range(1, n + 1):
    total += i

print(total)





















