# 1)შექმენით სია 10 ელემენტი, nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], შემდეგ  მასში ჩაამატეთ 10 ელემნტი, და ამოიღეთ  5 ელემენტი pop ით

# 2)შექმენით სია 10 ელემენტი, nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], შემდეგ  მასში ჩაამატეთ 10 ელემნტი, და ამოიღეთ  5 ელემენტი remove ით

# 3)შექმენით სია 10 ელემენტი, nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], შემდეგ  მასში ჩაამატეთ 10 ელემნტი insert ით  შშუაშუ, და ამოიღეთ  5 ელემენტი remove ით და 5 pop ით

# 4)colors = ["red", "green", "blue", "yellow", "purple"]
# თქვენი დავალებაა სიიდან წაშალოთ ბოლო ელემენტი .pop() მეთოდის დახმარებით, შემდეგ კი დაბეჭდოთ განახლებული სია.

# 5)შექმენი სია nums = [10, 20, 30, 40].
# გამოიყენე append() რომ დაამატო 50.




nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(11,21):
    nums.append(i)



for i in range(5):
    nums.pop()

print(nums)



print("________2_________")



nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for i in range(11,21):
    nums.append(i)

nums.remove(1)
nums.remove(2)
nums.remove(3)
nums.remove(4)
nums.remove(5)

print(nums)


print("________3_________")


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for i in range(11,21):
    nums.insert(5,i)


nums.remove(16)
nums.remove(17)
nums.remove(18)
nums.remove(19)
nums.remove(20)


for i in range(5):
    nums.pop()


print(nums)

print("________4_______")


colors = ["red", "green", "blue", "yellow", "purple"]

colors.pop()

print(colors)


print("________5_______")



nums = [10, 20, 30, 40]

nums.append(50)

print(nums)



