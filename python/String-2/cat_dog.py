# Return True if the string "cat" and "dog" appear the same number of times in the given string.
def cat_dog(str):
    dog_counter = cat_counter = 0
    for i in range(len(str)-2) :
        str3 = str[i:i+3]
        if str3 == 'dog' :
            dog_counter += 1
        elif str3 == 'cat' :
            cat_counter += 1
            
    if dog_counter == cat_counter : 
        return True
    return False