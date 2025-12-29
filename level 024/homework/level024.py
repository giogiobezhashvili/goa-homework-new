# 1

num=int(input("შემოიყვანე რიცხვი:"))


if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 2

num = 0

while num >= 0:
    num = int(input("Enter a number: "))
    if num >= 0:
        print("Positive number entered")
    else:
        print("Negative number entered. Program stopped.")

# 3

my_pin = "gio123"
num = 3

while num > 0:
    pin = input("enter PIN:")
    if pin == my_pin:
        print("access granted")
        break
    else:
        num -= 1


if num == 0:
    print("access denied")



# 4

fruits = ["ვაშლი", "ბანანი", "ატამი", "მსხალი", "ალუბალი"]

print(fruits[2])

# 5

numbers = [10, 20, 30, 40, 50]
numbers[1] = 25
print(numbers)


# 6

colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "იასამნისფერი"]
index = int(input("Enter index (0-4): "))
print(colors[index])


# 7

animals = ["ძაღლი", "კატა", "სპილო", "ვეფხვი", "ლომი"]
animals[-1] = "გემი"
print(animals)

# 8

colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]

index = int(input("Enter index: "))
new_color = input("Enter new color: ")

colors[index] = new_color
print(colors)
















