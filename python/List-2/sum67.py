# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
def sum67(nums):
    if nums :
        flag_67 = False
        result = 0
        for i in range(len(nums)) :
            if nums[i] != 6 :
                if not flag_67 :
                    result += nums[i]
                if nums[i] == 7 :
                    flag_67 = False
            else :
                flag_67 = True
        return result
    else :
        return 0
