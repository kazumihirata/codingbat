# Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
def first_last6(nums):
    size = int(len(nums)-1)
    
    return nums[0] == 6 or nums[size] == 6