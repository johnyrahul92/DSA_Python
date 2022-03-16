import math


def find_second_smallest(array):
    array_len=len(array)
    first = second = math.inf

    if array_len < 2:
        return("Input is not proper")
    
    for i in range(array_len):
        if array[i] < first:
            second= first
            first= array[i]
        elif (array[i] < second) and (array[i] != first):
            second =array[i]

    return first,second



arr =[1,-3,-3,4,-1,5,0.,9]

print(find_second_smallest(arr))