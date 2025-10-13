# == ოპერატორი ამოწმებს, ტოლია თუ არა ორი მნიშვნელობა
# != ოპერატორი ამოწმებს, განსხვავებულია თუ არა ორი მნიშვნელობა

print(5 == 5)      
print(10 == 7)     
print("გიო" == "გიო")


print(5 != 3)      
print(7 != 7)      
print("გიო" != "ნიკა") 


# Conditional Statement — ნიშნავს, რომ პროგრამა იღებს გადაწყვეტილებას გარკვეული პირობის მიხედვით.
# მთავარია if, elif, else — ეს 3 keyword

# if — თუ 
# elif — სხვა შემთხვევაში თუ 
# else — სხვა ყველა შემთხვევაში 


age = 20

if age > 18:  
    print("სრულწლოვანი ხარ ")
elif age == 18:  
    print(" 18  წლის ხარ")
else:  
    print("სრულჭლოვანი არ ხარ")





age = int(input("Enter your age: "))



if age > 18:
    print("You are an adult!")
elif age == 18:
    print("You are 18yo!")
else:
    print("You are teenager!")




total = 0

for i in range(1, 7): 
    print(i)
    total += i 
print( total)



user_name = input("Enter your name: ")

my_name = "Giorgi"

if user_name == my_name:
    print("The names are the same")
else:
    print("The names are different")









