def myreduce(func, seq):
    result = seq[0]
    for item in seq[1:]:
        result = func(result, item)
    return result


lst =['sdfs','sdfsfsdf','sdf']
print(myreduce(lambda a,b: a+b,lst))


max_find = lambda a,b: a if (a > b) else b

lst =[23, 21, 47,11,42,13]

print(myreduce(max_find, lst))