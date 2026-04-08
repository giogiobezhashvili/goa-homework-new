# 1
def count_sheeps(sheep):
    result = 0
    
    for i in sheep:
        if i == True:
            result += 1
    return result

# 2
def sum_mix(arr):
    larr = []
    for  i in arr:
        i = int(i)
        larr.append(i)
    return sum(larr)

# 3
def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9 

# 4
def mouth_size(animal): 
    if animal.lower() == "alligator": 
        return "small"
    else:
        return  "wide"

# 5
def digitize(n):
    result = []
    for i in str(n):
        result.insert(0, int(i))
    return result