print("Bracket Chnages")
open_list=["{","(","["]
close_list=["}",")","]"]

def bracket_validator(input):
    stack=[]
    for i in input:

        if i in open_list:
            stack.append(i)
        elif i in close_list:
            stack_len= len(stack)
            pos=close_list.index(i)
            if stack_len>0 and stack[stack_len-1] == open_list[pos]:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

print(bracket_validator("({})"))