s1='abdc'
s2='adcba'

def check(s1: str,s2 :str):
    if sorted(s1)==sorted(s2):
        return True
    else:
        return False


print(check(s1,s2))

input=['cat','dog','cat','god']
input=list(set(input))
print(input)

# final_list=[]
# for i in input:

#     if 
#     print (i)