# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
def sum13(nums):
    if nums :
        flag_13 = False
        result = 0
        for i in range(len(nums)) :
            if nums[i] != 13 :
                if flag_13 :
                    flag_13 = False
                else :
                    result += nums[i]
            else :
                flag_13 = True
        return result
    else :
        return 0
