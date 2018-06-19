# Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
def last2(str):
    elems = []
    for i in range(len(str)-2) :
        elems.append(str[i:i+2])
    
    cnt = 0
    for j in elems :
        if j == str[-2:] :
            cnt = cnt + 1
    return cnt
