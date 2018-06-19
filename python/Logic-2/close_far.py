# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.
def close_far(a, b, c):
  # int a, b and c
  # return True if b or c is "close"
  # ### "close" : aとくらべて1以上離れている場合
  # ### "far" : close以外
  # close_far(1, 2, 10) → True
  # 1 , 2 -> close -> True
  # 1, 10 -> far
  # close_far(1, 2, 3) → False
  # 1, 2 -> close
  # 1, 3 -> 
  if abs(a-b)<=1 and abs(a-c) >= 2 and abs(c-b) >= 2 :
    return True
    
  if abs(a-c)<=1 and abs(a-b) >= 2 and abs(c-b) >= 2 :
    return True
    
  return False

  
