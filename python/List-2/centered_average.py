# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.
def centered_average(nums):
    if len(nums) < 3 :
        return 0
    else :
        # remove max and min values
        pos_max = nums.index(max(nums))
        del nums[pos_max]
        pos_min = nums.index(min(nums))
        del nums[pos_min]
        
        # remove duplicates
        nums_uniq = list(set(nums))
        
        result = 0
        for i in range(len(nums_uniq)) :
            result += int(nums_uniq[i])
        if result :
            result = int(result / len(nums_uniq))
        return result