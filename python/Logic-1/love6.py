# The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.
def love6(a, b):
  sum = a + b
  diff = abs(a - b)
  
  if a == 6 or b == 6 :
    return True
  elif sum == 6 or diff == 6 :
    return True
  else :
    return False
