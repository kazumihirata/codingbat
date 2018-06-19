# Return the number of times that the string "hi" appears anywhere in the given string.
def count_hi(str):
    li = [str[i:i+2] for i in range(len(str)-1)]
    counter = 0
    for j in range(len(li)) :
        if li[j] == 'hi' :
            counter+= 1
    return counter