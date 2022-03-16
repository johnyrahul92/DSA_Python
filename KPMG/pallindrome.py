


def check_pallidrome(input):
    stack=[]
    i=0
    mid=len(input)//2
    input_len=len(input)
   

    while i<mid:
        stack.append(input[i])
        i+=1
    
    if input_len%2:
        mid+=1

    while input_len > mid:
        if not (stack.pop() == input[mid]):
            return False
        mid+=1

    return True


print(check_pallidrome("abcdcba"))

