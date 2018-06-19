# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
def first_half(str):
    if len(str) > 0 :
        halfPosition = int(len(str) / 2)
        return str[:halfPosition]
    else :
        return str