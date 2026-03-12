# 1
def abbrev_name(name):
    first,last = name.split()
    return f"{first[0].upper()}.{last[0].upper()}"

# 2

def litres(time):
    return (time * 0.5) //1

# 3

def find_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

# 4

def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0 


# 5
def divisors(n: int):
    result = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            result.append(i)

            if i != n // i:
                result.append(n // i)
    return sorted(result) if result else f"{n} is prime"
