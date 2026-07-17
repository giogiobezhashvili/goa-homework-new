# 1
def is_kiss(words):
    new_wd= words.split()
    len_w= len(new_wd)
    
    for i in new_wd:
        if len(i) >  len_w:
            return "Keep It Simple Stupid"
        
    return "Good work Joe!"
