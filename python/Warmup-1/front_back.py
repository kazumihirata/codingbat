# Given a string, return a new string where the first and last chars have been exchanged.
def front_back(str):
  if len(str) == 0 :
    return str
  elif len(str) == 1 :
    return str
  elif len(str) == 2 :
    return str[1] + str[0]
  else :
    return str[-1] + str[1:-1] + str[0]
