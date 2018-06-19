# Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
def extra_end(str):
    if len(str) >= 2 :
        last2 = str[-2:]
        return last2 * 3
    else :
        return str
