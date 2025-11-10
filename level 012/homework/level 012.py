# 1) შედარებითი ოპერატორები (Comparison Operators)

# ==  — ამოწმებს ტოლია თუ არა ორი მნიშვნელობა
print(5 == 5)   
print(7 == 3)  
print("a" == "a")  
print(10 == 10.0)  
print(2 + 3 == 5) 

# != — ამოწმებს არათანაბრობას
print(5 != 3)   
print(5 != 5)  
print("a" != "b")  
print(10 != 11)  
print(1 + 1 != 3) 

# > — მეტობა
print(10 > 5)  
print(3 > 7)   
print(8 > 8)   
print(9 > 2)  
print(100 > 99) 

# < — ნაკლებობა
print(2 < 5)   
print(5 < 2)   
print(7 < 7)   
print(1 < 9)  
print(3 < 10)  

# >= — მეტია ან ტოლია
print(5 >= 5)   
print(6 >= 2)   
print(1 >= 4)  
print(10 >= 10) 
print(3 >= 5)   

# <= — ნაკლებია ან ტოლია
print(5 <= 5)   
print(2 <= 6)   
print(9 <= 4)   
print(10 <= 10) 
print(1 <= 7)   





# 2 
#Logical operators ესენი გვაძლევენ შედეგს True ან False


# and — აბრუნებს True-ს მაშინ, როცა ორივე პირობა დაკმაყოფილებულია
# or — აბრუნებს True-ს მაშინ, როცა რომელიმე პირობა აკმაყოფილებს



# 3

# and მაგალითები
print(5 > 3 and 10 > 7)   
print(5 > 3 and 2 > 9)   
print(1 == 1 and 2 == 2)  

# or მაგალითები
print(5 > 10 or 2 < 9)    
print(3 == 3 or 4 == 5)  
print(1 > 2 or 2 > 3)     

 


# 4
my_number = 10
user_number = int(input("შეიყვანე რიცხვი: "))

if user_number > my_number:
    print("შენი რიცხვი მეტია ჩემსაზე!")
else:
    print("შენი რიცხვი არ არის მეტ ჩემი რიცხვზე.")


# 5
my_name = "გიორგი"
user_name = input("შეიყვანე შენი სახელი: ")

if user_name == my_name:
    print("ჩვენ ერთი სახელი გვაქვს!")
else:
    print("ჩვენ სხვადასხვა სახელები გვაქვს.")


# 6
age = int(input("შეიყვანე შენი ასაკი: "))

if age > 18:
    print("შენ სრულწლოვანი ხარ.")
else:
    print("შენ ჯერ არ ხარ სრულწლოვანი.")