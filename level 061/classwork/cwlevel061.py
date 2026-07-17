# 1
def sum_of_minimums(numbers):
    total = 0 
    for i in numbers:
        total += min(i)
    return total
# 2
def vaporcode(s):
    return "  ".join(s.replace(" ","").upper())
# 3
def reverse_words(text):
    res = []
    for i in text.split(' '):
        res.append(i[::-1])
    return " ".join(res)  
# 4
def spin_words(s):
    res = []
    
    for i in s.split(" "):
        if len(i) >= 5:
            res.append(i[::-1])
        else:
            res.append(i)
    return " ".join(res)