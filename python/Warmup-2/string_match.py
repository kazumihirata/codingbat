# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
def string_match(a, b):
    # always (a > b)
    if len(a) < len(b) :
        tmp = a
        a = b
        b = tmp
        
    counter = 0
    for i in range(len(b)-1) :
        sliceA = a[i:i+2]
        sliceB = b[i:i+2]
        
        if sliceA == sliceB :
            counter = counter + 1
    return counter