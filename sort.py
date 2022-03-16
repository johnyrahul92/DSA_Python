list_of_objects=[
    {'a':1},
    {'a':2},
    {'a':3},
]

def my_key(e):
    return e['a']


list_of_objects.sort(key=my_key,reverse=True)

print(list_of_objects)