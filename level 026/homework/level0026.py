# 1
num = [3, 4, 6, 8, 7,]

print(num)

s_num = 0

for i in num:
    s_num += i

print(s_num)

print("________2_______")
# 2

num = [5,4,3,6,7,9]

x = 0

for i in num:
    if i % 2 == 0:
        x += 1
print(x)


print("________3_______")    
# 3

numbers = [1,3,5,4,2,6,8,7]


min_num = numbers[0]
max_num = numbers[0]

for num in numbers:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num


print( min_num)
print( max_num)


print("________4_______")
# 4

num = [3,4,5,6,7,8,9]

for i in num:
    if i % 2 != 0:
        print(i)


print("________5_______")

# 5

s_num = 0

while True:
    num = int(input("შეიყვანე რიცხვი:"))
    if num == 0 :
        break
    s_num += num

print(s_num)


print("_______6________")
# 6

while True:
    num = int(input("შეიყვანე რიცხვი:"))
    if num < 0:
        break



print("_______7________")

# 7

while True:
    num = int(input("შეიყვენე რიცხვი:"))
    if num % 5 == 0:
        break


print("_______8________")
# 8

h = 0

while True:
    num = int(input("შეიყვანე რიცხვი:"))
    h += 1
    if num % 2 == 0:
        break

print(h)

print("_______9________")
# 9

while True:
    num = int(input("შეიყვანე რიცხვი:"))
    if num % 2 != 0:
        break


print("_______10________")

# 10

while True:
    num = int(input("შეიყვანე რიცხვი:"))
    if num < 0:
        continue
    if num == 0:
        break
print(num)


print("_______11________")
# 11

while True:
    num = int(input("შეიყვანე რიცხვი:"))
    if num < 0:
        continue
    if num == 100:
        break

print("num")

