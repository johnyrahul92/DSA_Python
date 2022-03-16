

def bs(lo,hi, condition):

    while lo<=hi:
        mid= (lo+hi)//2

        
        result= condition(mid)
        print('lo:',lo,'hi:',hi,'mid:',mid,'result:',result)
        if result == 'found':
            return mid
        elif result == 'left':
            hi=mid-1
        else:
            lo=mid+1
    
    return -1

def locate_query_pos(input,query):
    def condition(mid):

        if input[mid] == query:
            if mid-1 >= 0 and input[mid-1]== query:
                return 'left'
            else:
                return 'found'
        elif input[mid] > query:
            return 'left'
        else:
            return 'right'

    return bs(0,len(input)-1,condition)

input_arr=[0,1,2,2,2,3,4]
query= 2

print(locate_query_pos(input_arr,query))
      


    