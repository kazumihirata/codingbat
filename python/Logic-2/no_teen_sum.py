# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().
def fix_teen(n):
    target = [13, 14, 17, 18, 19]
    return n in target

def no_teen_sum(a, b, c):
    result = 0
    if not fix_teen(a) : result += a
    if not fix_teen(b) : result += b
    if not fix_teen(c) : result += c
    return result