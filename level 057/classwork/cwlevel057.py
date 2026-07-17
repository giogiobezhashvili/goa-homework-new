# 1
def divisors(n):
    count = 0 
    
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count
# 2
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))
# 3