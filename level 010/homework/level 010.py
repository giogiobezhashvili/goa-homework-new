# 2) Boolean მონაცემთა ტიპი
# Boolean არის მონაცემთა ტიპი, რომელსაც შეუძლია მიიღოს მხოლოდ ორი მნიშვნელობა: True ან False
# True ნიშნავს "სიმართლე", ხოლო False ნიშნავს "მცდარი".


# 3) Binary code
# Binary code წარმოადგენს სისტემას, სადაც ინფორმაცია გამოიხატება მხოლოდ ორ ციფრით: 0 და 1.
# 1 ნიშნავს ჩართული (ON) მდგომარეობას, ხოლო 0 ნიშნავს გამორთულ (OFF) მდგომარეობას.


# 4) bool() ფუნქცია
# bool() ფუნქცია გამოიყენება იმისათვის, რომ მნიშვნელობა გადავაქციოთ Boolean ტიპად.


# 5)
a = 10
b = 15
print(a == b)  

# 6) 
num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

if num1 > num2:
    print("პირველი რიცხვი უფრო დიდია.")
elif num1 < num2:
    print("მეორე რიცხვი უფრო დიდია.")
else:
    print("რიცხვები ტოლია.")

# 7) 
word = input("შეიყვანე სიტყვა: ")
if word == "Python":
    print("სიტყვა ემთხვევა 'Python'-ს")
else:
    print("სიტყვა არ ემთხვევა")

# 8) 
num = int(input("შეიყვანე რიცხვი: "))
if num > 100:
    print("რიცხვი მეტია 100-ზე")
else:
    print("რიცხვი 100-ზე ნაკლებია ან ტოლია")

# 9)
password = input("შეიყვანე პაროლი: ")
if password == "gi2009":
    print("პაროლი სწორია ")
else:
    print("პაროლი არასწორია ")

# 10)
x = int(input("პირველი რიცხვი: "))
y = int(input("მეორე რიცხვი: "))

print("პირველი მეტია მეორეზე:", x > y)
print("პირველი ნაკლებია მეორეზე:", x < y)
print("პირველი ტოლია მეორესთან:", x == y)

# 11)
s1 = input("შეიყვანე პირველი ტექსტი: ")
s2 = input("შეიყვანე მეორე ტექსტი: ")
s3 = input("შეიყვანე მესამე ტექსტი: ")
s4 = input("შეიყვანე მეოთხე ტექსტი: ")
s5 = input("შეიყვანე მეხუთე ტექსტი: ")

result = s1 + s2 + s3 + s4 + s5
print(result)

# 12) 
n1 = float(input("პირველი რიცხვი: "))
n2 = float(input("მეორე რიცხვი: "))
n3 = float(input("მესამე რიცხვი: "))
n4 = float(input("მეოთხე რიცხვი: "))

პასუხი= (n1 + n2 + n3 + n4) / 4
print(პასუხი)

# 13)
a = 10          
b = 5.5          
c = "Python"      
d = True         

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 14) 
str1 = "Hello"
str2 = "hello"
print(str1 == str2)  

# 15) 
x1 = "40"
x2 = "50"
x3 = "30"
x4 = "10"

sum_result = int(x1) + int(x2) + int(x3) + int(x4)
print(sum_result)

# 16)
n1 = 30
n2 = 40
n3 = 50
print(str(n1) + str(n2) + str(n3))  