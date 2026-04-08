# 1
def remove_smallest(numbers):
    if not numbers:
        return []
    
    b = numbers.index(min(numbers))
    return numbers[:b] + numbers[b+1:]

# 2
def number(lines):
    result = []
    
    for i in range(len(lines)):
        result.append(str(i+1) + ": " +lines[i])
        
    return result

