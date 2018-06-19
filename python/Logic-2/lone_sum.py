# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.
def lone_sum(a, b, c):
    result = 0
    if not a == b and not a == c :
        result += a
    if not b == a and not b == c :
        result += b
    if not c == a and not c == b :
        result += c
    return result