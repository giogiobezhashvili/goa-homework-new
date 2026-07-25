# 1
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump:
        return True 
    else:
        return False
    
# 2
def sum_array(arr):
    if arr is None or len(arr) < 3:
        return 0
    else:
        return sum(arr) - max(arr) - min(arr)
# 3
def double_char(s):
    res = ""
    for i in s:
        res += i * 2
    return res
# 4
def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2)
# 5
def is_even(n): 
    if n == 0 :
        return True
    else:
        return n % 2== 0
    
