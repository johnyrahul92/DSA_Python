

def strings1(input, count):
    start = 0
    input_len = len(input)
    final_list = []
    while (start + count) <= input_len  :
        n=0
        s = ''
        inc=start        
        while n<count :
            s=s+input[inc]
            n+=1
            inc+=1
        start+=1
        final_list.append(s)
    return final_list

input ="abcdfeg"
count =3

print(strings1(input,count))

output=['ab','bc']


