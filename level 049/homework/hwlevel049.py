# 1
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return  i
        
# 2

def summation(num):
    jami = 0 
    for i in range(1, num + 1):
        jami += i
    return jami
    
# 3.1

def rps(p1, p2):
    
    if p1 == p2:
        return  'Draw!'
    elif p1 == 'scissors' and p2 == 'rock':
        return "Player 2 won!"
    elif p1 == 'rock' and p2 == 'scissors':
        return  "Player 1 won!"
    
    elif p1 == 'paper' and p2 == 'rock':
        return "Player 1 won!"
    elif p1 == 'rock' and p2 == 'paper':
        return  "Player 2 won!"
    
    elif p1 == 'scissors' and p2 == 'paper':
        return "Player 1 won!"
    elif p1 == 'paper' and p2 == 'scissors':
        return  "Player 2 won!"
    
# 3.2

def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif p1 == 'rock' and p2 == 'scissors':
        return "Player 1 won!"
    elif p1 == 'scissors' and p2 == 'paper':
        return "Player 1 won!"
    elif p1 == 'paper' and p2 == 'rock':
        return "Player 1 won!"
    else:
        return "Player 2 won!"


# 4

def to_jaden_case(string):
    
    word =  string.split()
    result = []
    
    for i in word:
        result.append(i.capitalize())
        
    return " ".join(result)


# 5


def cap_me(arr):
    result = []
    
    for name in arr:
        result.append(name.capitalize())
    return result
