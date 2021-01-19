# def decorator_bread(func):
#     def wrapper():
#         print('bread')
#         func()
#         print('bread')
#     return wrapper

# def decorator_vegtables(func):
#     def wrapper():
#         print('tommatoes')
#         func()
#         print('salad')
#     return wrapper

# @decorator_bread
# @decorator_vegtables
# def ham():
#     print('ham')

# ham()

# def bold(func):
#     def wrapper():
#         return 'b' + func() + 'b'
#     return wrapper

# def italic(func):
#     def wrapper():
#         return 'i' + func() + 'i'
#     return wrapper

# @bold
# @italic
# def hello():
#     return 'hello'

# print(hello())

# a = [2,2]
# a.sum()

def decorator(func):
    def wrapper(arg1, arg2):
        print(arg1, arg2)
        func(arg1, arg2)
    return wrapper


@decorator
def abc(ac, bc):
    return print(ac, bc)


abc('hi', 'hello')

# def abc(*args, **kwargs):
#     return kwargs

# print(abc(a = 123, b = 123, d= 123))
