# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.
def end_other(a, b):
    if len(a) < len(b) :
        return a.lower() in b[((len(a))*-1):].lower()
    else :
        return b.lower() in a[((len(b))*-1):].lower()
    # return (b.lower().endswith(a.lower()) or a.lower().endswith(b.lower()))