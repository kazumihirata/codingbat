# Given an array of ints length 3, return the sum of all the elements.
def sum3(nums):
  result = 0
  for i in range(len(nums)) :
    result = result + nums[i]
  return result
