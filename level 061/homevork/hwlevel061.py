# 1
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump
# 2
def sum_array(arr):
    if type(arr) != list:
        return 0
    if len(arr) < 3:
        return 0
    arr = sorted(arr)
    min = arr[0]
    max = arr[-1]
    return  sum(arr) - min - max
# 3
def double_char(s):
    res = ""
    
    for i in s:
        res += i *2
    return res
# 4
def array_plus_array(arr1,arr2):
    return sum(arr1 + arr2)
# 5
def is_even(n): 
    # your code here
    if n % 2 == 0:
        return True
    else:
        return False
