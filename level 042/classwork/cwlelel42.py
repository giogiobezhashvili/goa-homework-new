# 1

def make_upper_case(s):
    return s.upper()

# 2

def summation(num):
    jami = 0 
    for i in range(1, num + 1):
        jami += i
    return jami
    
# 3
def to_alternating_case(string):
    result = ""
    for i in string:
        if i == i.lower():
            result += i.upper()
        elif i == i.upper():
            result += i.lower()
        else:
            result += i
    return result
# 4
def find_needle(haystack):
    position = haystack.index("needle")
    return f"found the needle at position {position}"

# 5

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2

















