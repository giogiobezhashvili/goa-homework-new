# 1)
def add_length(str):
    words = str.split()
    result = []
    
    for word in words:
        result.append(f"{word} {len(word)}")
    
    return result

# 2)
def invert(lst):
    result = []
    for i in lst:
        result.append(i* -1)
    return result

# 3)
def divisible_by(numbers, divisor):
    result = []
    
    for i in numbers:
        if i % divisor == 0:
            result.append(i)
    return result

# 4)
def square_sum(numbers):
    result = []
    for i in numbers:
        i = i ** 2
        result.append(i)
    return sum(result)

# 5)
def positive_sum(arr):
    jami = 0 
    for i in arr:
        if i > 0:
            jami += i   
    return jami