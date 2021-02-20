def myfilter(func, seq):
    for i in seq:
        if func(i) == True:
            yield i

number_list = range(-5, 5)
less_than_zero = list(myfilter(lambda x: x < 0, number_list))
print(less_than_zero)