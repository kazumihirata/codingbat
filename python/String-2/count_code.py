# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
def count_code(str):
    li = [str[i:i+4] for i in range(len(str)-3)]
    counter = 0
#     print(li)
    for j in range(len(li)) :
#         print(li[j])
#         print(li[j][:1])
#         print(li[j][1:2])
#         print(li[j][-1:])
#         print(type(li[j][:0]))
#         print(type('c'))
#         if (li[j][:1] in ['c']) and (li[j][1:2] in ['o']) and (li[j][-1:] in ['e']) :  # OK
        if (li[j][:1] == 'c') and (li[j][1:2] == 'o') and (li[j][-1:] == 'e') :      # NG
#         if (li[j][:0] is 'c') and (li[j][1:2] is 'o') and (li[j][-1:] is 'e') :            # NG
            counter = counter + 1
#         print('-----')
    return counter