

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

      


    