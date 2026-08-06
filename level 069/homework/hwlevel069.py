# 1
def is_isogram(s):
    s_n = s.lower()
    return len(set(s_n)) == len(s_n)
# 2
def fizzbuzz(n):
    res = []
    
    for i in range(1, n +1):
        if i % 3 == 0 and i % 5 == 0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(i)
    return res
# 3
def two_oldest_ages(ages):
    ages.sort()
    return [ages[-2], ages[-1]]
# 4
def squares(x, n):
    if n <= 0:
        return []
    res = [x]
    
    for i in range(1, n):
        res.append(res[-1] ** 2)
    return res
# 5
