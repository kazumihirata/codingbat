# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
def array123(nums):
    one_flag = False
    two_flag = False
    three_flag = False
    
    if 1 in nums :
        one_flag = True
    if 2 in nums :
        two_flag = True
    if 3 in nums :
        three_flag = True
    if one_flag and two_flag and three_flag :
        return True
    else :
        return False