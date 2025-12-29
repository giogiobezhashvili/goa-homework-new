# 1

for i in range(0, 39): 
    print(i)

# 2

for i in range(30,40):
    print(i)

# 3

for i in range(12,121):
    print(i)

# 4

name= "gio"
age = 16

for i in range(18):
    print(name,age)
    # ან მეორე სახით მეორე პრინტი დაბლა დაუწეროთ და მივუთითოთ age 

# 5

for i in range(10, 101, 3): 
    print(i)


# 6
fruit="ფორტოხალს"

for i in range(1, 31):  
    print(i, fruit)

# 7

age=input("შეიყვანე შენი ასაკი:" )

for i in range(13):
    print(age)

# 8


name= "gio"
i=0
while i <= 9:
    print(name)
    i += 1


#  9


num= 0 

while num <= 24 :
    print(num)
    num += 1


# 10 



for i in range(1, 101):
    if  i % 3 == 0 and i % 5 == 0 :
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


for i in range(2, 201, 2):
    if i == 152:
        break
    print(i)



li=[2, 12, 30, 3, 37, 69, 67]
maximum = li[0]

for i in li :
    if i > maximum:
        maximum= i 

print(maximum)




text = "giorgi"
count= 0

for i in text:
    if i.isupper():
        count += 1

print(count) 




num = 100

while num >= 1:
    print(num)
    num -= 1






