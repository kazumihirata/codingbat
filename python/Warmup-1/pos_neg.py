# Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
def pos_neg(a, b, negative):
    a_symbol = 0
    b_symbol = 0
    if a == 0 :
        pass
    elif a > 0 :
        a_symbol = 1

    if b == 0 :
        pass
    elif b > 0 :
        b_symbol = 1

    if negative :
        if a_symbol == 0 and b_symbol == 0 :
            return True
        else :
            return False
    else :
        if not a_symbol == b_symbol :
            return True
        else :
            return False