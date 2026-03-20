# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print("Before the function runs")
#         result = original_function(*args, **kwargs)
#         print("After the function runs")
#         return result
#     return wrapper_function

# @decorator_function
# def say_hello(name):
#     print(f"Hello {name}")

# say_hello("Turab")

######################## firs example

# def func():
#       print("hello")

# printFuncValue = func
# printFuncValue()

######################## Second Example
# def my_decoraters(func):
#       def wrapper(*args, **kwargs):
#             print("Before Function")
#             result = func(*args, **kwargs)
#             print("After Function")
#             return result
#       return wrapper

# @my_decoraters
# def Func():
#       print("hello world")
# Func()

import time

def timmer(func):
      def wrapper(*args, **kwargs):
            args_value = " ,".join(str(arg) for arg in args)
            # args_value = " ,".join(str(arg) for arg in args)
            # print(args_value) 
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"function is {func.__name__} with {args_value} arguments and time is {end-start}")
            # print("function if {func.__name__} ",{end-start}, *args)

            # return result
      return wrapper

@timmer
def func(val1, val2):
      print(val1, val2)

func("new world", "hello world")

# @timmer
# def func2(val1, val2):
#       print(val1*val2*val1*val2*val1*val2*val1*val2*val1*val2*val1*val2)

# func2(4000, 90000)


# @timmer
# def timmerFunc(num):
#       time.sleep(num)
#       print("num::", num)

# timmerFunc(2)




# @timmer
# def timmerFunc(num):
#       # time.sleep(num)
#       print("num:::::", num)

# timmerFunc(2)