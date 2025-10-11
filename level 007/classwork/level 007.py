from turtle import *


# input - შემავალი ინფორმაცია
# output - გამომავალი ინფორმაცია


#  კონკატინაცია არის ორი სტრინგით შეერთებული სიტყვა
# print(str("gio")+str("bezhashvili"))

name=input("name :")
name2=input("surname :")
name3=input("age :")
name4=input("place of residence :")
name5=input("favorite color:")
name6=input("favorite car:")
print(name+name2+name3+name4+name5+name6)


# 1/5
num1 = "10"
num2 = int(num1) 
print(num1, type(num2)) 

# 2/5
num2 = "25"
num3 = int(num2)  
print(num2, type(num3)) 

# 3/5
num3 = "100"
num4 = int(num3)  
print(num3, type(num4)) 

# 4/5
num4 = "0"
num5 = int(num4)  
print(num4, type(num5))  

# 5/5
num5 = "5"
num6 = int(num5)  
print(num5, type(num6))  





num1 = 55
num1 = str(num1)
print(num1, type(num1))  # '55' <class 'str'>


num2 = -99
num2 = str(num2)
print(num2, type(num2))  # '-99' <class 'str'>


num3 = 7
num3 = str(num3)
print(num3, type(num3))  # '7' <class 'str'>


num4 = 99
num4 = str(num4)
print(num4, type(num4))  # '99' <class 'str'>


num5 = 5
num5 = str(num5)
print(num5, type(num5))  # '5' <class 'str'>






user_input = input("შემოიტანეთ რიცხვი: ")


number = int(user_input)


result = number + 15
print("თქვენი რიცხვი გაზრდილი 15-ით არის:", result)


user_input = input("შემოიტანეთ რიცხვი: ")


number = int(user_input)


result = number + 15

print(- result)


