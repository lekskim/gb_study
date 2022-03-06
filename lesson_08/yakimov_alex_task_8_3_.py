
def type_logger(func):

    def logger(*args, **kwargs):
           if func.__name__== 'render_input':
               print(f'Call for: {func.__name__}')
               print(f'{args[0]}: {type(func(*args, **kwargs))} ')
               for i in kwargs:
                   print(f"'{i}' = {kwargs.get(i)}: {type(kwargs.get(i))}, ", end='')
               print('\n', f'Rezult: {func(*args, **kwargs)} type: {type(func(*args, **kwargs))}')
           else:
               print(f'Call for: {func.__name__}')
               print(f'{args[0]}: {type(func(*args, **kwargs))} ')
               print(f'Rezult: {func(*args, **kwargs)} type: {type(func(*args, **kwargs))}')
    return logger


@type_logger
def render_input(*args, **kwargs):
   return 1

@type_logger
def calc_cube(x):
   return x ** 3


#@type_logger
#def calc_cube(x):
 #  return x ** 3


#>>> a = calc_cube(5)
#Call for: calc_cube
#5: <class 'int'>
#Rezult: 125  type: <class 'int'>

#>>> render_input(1, a = 2, b = True, c = "q")
#Call for: render_input
#1: <class 'int'>
#'a' = 2: <class 'int'>, 'b' = True: <class 'bool'>, 'c' = q: <class 'str'>
#Rezult: 1  type: <class 'int'>





