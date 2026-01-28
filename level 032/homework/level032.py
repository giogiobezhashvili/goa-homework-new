# .append() — სიის ბოლოში ამატებს ახალ ელემენტს
# .insert() — სიის კონკრეტულ პოზიციაზე  ამატებს ელემენტს
# .pop() — შლის სიის ბოლო ელემენტს



print("________1________")


num = ["gio","nika","luka","lasha"]

print(len(num))


print("________2_________")


numbers = []

for i in range(5):
    num = int(input("შეიყვანეთ რიცხვი: "))
    numbers.append(num)

print(numbers)


print("________3_________")


colors = ["red", "green", "blue", "yellow", "purple"]

colors.pop()
print(colors)

print("________4_________")

animals = ["dog", "cat", "elephant", "lion"]

animals.insert("monkey")
print(animals)


print("________5_________")

students = []

for i in range(3):
    name = input("შეიყვანე შენი სახელი:")
    students.append(name)

students.insert(0, "teacher")
students.pop()
print(len(students))
print(students)



























