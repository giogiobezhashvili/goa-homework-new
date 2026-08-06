# 1
def monkey_count(n):
    res = []
    for i in range(1, n+1):
        res.append(i)
    return res
# 2
def square_digits(num):
    res = ""
    n_num = str(num)
    for i in n_num:
        n = int(i) ** 2
        a = str(n)
        res += a
    return int(res)
# 3
def friend(x):
    res = []
    for i in x:
        if len(i) == 4:
            res.append(i)
    return res

# 4
def create_phone_number(n):
    res = ""
    
    for i in n:
        res += str(i)
        
    return f"({res[:3]}) {res[3:6]}-{res[6:]}"
