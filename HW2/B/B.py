def solution(x):
    x = x.replace("h", "H")
    
    oldstring = x
    newstring = ""
    for i in range (0, len(oldstring)):
        if i % 3 != 0:
            newstring = newstring + oldstring[i]
            
    newstring = newstring.replace(1, "one")
    return newstring
