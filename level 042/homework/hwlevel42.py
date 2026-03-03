# 1
def remove_exclamation_marks(s):
    return s.replace("!","")

# 2

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump

# 3
def distinct(seq):
    seq = set(seq) 
    return list(seq)
# 4

def distinct(seq):
    seen = set()
    result = []
    
    for i in seq:
        if i not in seen:
            seen.add(i)
            result.append(i)

    return result


# 5


def bmi(weight, height):
    index = weight / height**2   
    if index <= 18.5:
        return "Underweight"
    elif index <= 25.0:
        return "Normal"
    elif index <= 30.0:
        return "Overweight"
    else:
        return "Obese"
        



