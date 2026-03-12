# 1
import math

def square_or_square_root(arr):
    result = []
    
    for num in arr:
        root = math.sqrt(num)
        
        if root == int(root):
            result.append(int(root))
        else:
            result.append(num * num)
            
    return result
# 2
def sum_mix(arr):
    result = []
    
    for i in arr:
        i = int(i)
        result.append(i)
    return sum(result)

# 3

def logical_calc(array, op):
    result = array[0]
    
    for i in  array[1:]:
        if op =="AND":
            result = result and i
        elif op == "OR":
            result = result or i
        elif op == "XOR":
            result = result != i
    return result

# 4

def calculator(x, y, op):
    if type(x) == str or  type(y) == str:
        return "unknown value"
    
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x / y
    else:
        return "unknown value"
    
# 5

def count_sheep(n):
    result = ""
    
    for i in range(1,n+1):
        result += f"{i} sheep..."
    return result