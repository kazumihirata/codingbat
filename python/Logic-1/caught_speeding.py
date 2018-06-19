# You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
def caught_speeding(speed, is_birthday):
  # value: 0=no ticket, 1=small ticket, 2=big ticket
  limit1 = 60
  limit2 = 80
  ticket = 0
  
  if is_birthday :
    limit1 = 65
    limit2 = 85
  
  if limit1 < speed and speed <= limit2 :
    ticket = 1
  elif limit2 < speed :
    ticket = 2
  return ticket
    
    
