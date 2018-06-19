# Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
def rotate_left3(nums):
    firstNum = nums[0]
    result = []
    for i in range(len(nums)-1) :
        result.append(nums[i+1])
    result.append(firstNum)
    return result