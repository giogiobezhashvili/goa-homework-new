
# 1
# Logical operators — გამოიყენება რამდენიმე პირობის შესამოწმებლად ერთდროულად.

# and → აბრუნებს True-ს მხოლოდ მაშინ, როცა ორივე პირობაა True
# or → აბრუნებს True-ს მაშინაც, როცა ერთ-ერთი პირობა მაინც True-ა.




# 2
name = input("შეიყვანე შენი სახელი: ")

if name == "გიო":
    print("მოგესმინე, შენ ხარ გიო!")
else:
    print("შენი სახელი არ არის გიო.")

# 3
number = int(input("შეიყვანე რიცხვი: "))

if number > 50:
    print("რიცხვი მეტია 50-ზე.")
else:
    print("რიცხვი 50-ზე ნაკლები ან ტოლია.")

# 4

toy = input("შეიყვანე შენი საყვარელი სათამაშო: ")
my_toy = "lego"

if toy == my_toy:
    print("ჩვენ ორივეს ერთი და იგივე სათამაშო გვიყვარს!")
else:
    print("ჩვენი საყვარელი სათამაშოები განსხვავდება.")


# 5
print(5 > 3)   
print(10 < 7)  
print(8 >= 8)  
print(4 <= 2)    
print(9 == 9) 



# 6

age = 20
has_id = True
print(age >= 18 and has_id)   

#6.2
is_student = False
has_discount = True
print(is_student or has_discount)  













