# 1

def simple_multiplication(number) :
    # Your code goes here
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9


# 2

def is_even(n): 
    # your code here
    if n % 2 == 0:
        return True
    else:
        return False

# 3


def basic_op(operator, value1, value2):
    #your code here
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2
    

# 4


def bool_to_word(boolean):
    # TODO
    if boolean == True:
        return "Yes"
    else:
        return "No"
    


# 5

def find_average(numbers):
    # your code here
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers) 



