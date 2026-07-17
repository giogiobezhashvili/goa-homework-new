# 1
def solution(text, ending):
    return text.endswith(ending)
# 2
def row_sum_odd_numbers(n):
    return n ** 3
# 3
def get_count(sentence):
    alf = "aeiou"
    count = 0 

    for i in sentence:
        if i in alf:
            count += 1
            
    return count
# 4
def sum_two_smallest_numbers(numbers):
    f_num = min(numbers)
    l = numbers.remove(f_num)
    s_num = min(numbers)
    return f_num + s_num
# 5
def abbrev_name(name):
    first, last = name.split()
    return f"{first[0].upper()}.{last[0].upper()}"
# 6
def player_rank_up(pts):
    if pts >= 100:
            return "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up."
    else:
        return False