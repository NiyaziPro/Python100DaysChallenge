def add(*args):  # *args - Arguments
    return sum(args)


print(add(4, 5, 6, 7, 8))


def calculate(n,**kwargs):  # kwargs - Keyword Arguments
    print(kwargs)


calculate(2,add=3, multiply=5)
