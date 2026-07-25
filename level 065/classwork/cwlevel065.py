# 1
def reverse_seq(n):
    return list(range(n,0,-1))

# 2
def rain_amount(mm):
    if mm < 40:
        return f"You need to give your plant {40 - mm}mm of water"
    else:
        return f"Your plant has had more than enough water for today!"
# 3
def correct(s):
    res = ''
    for i in s:
        if i == '0':
            res += 'O'
        elif i == '5':
            res += 'S'
        elif i == '1':
            res += 'I'
        else:
            res += i
            
    return res

# 4
def count_positives_sum_negatives(arr):
    count = 0
    total = 0 
    
    
    for i in arr:
        if i > 0:
            count += 1
        if i < 0:
            total += i
    return [count,total] if len(arr) != 0 else []



