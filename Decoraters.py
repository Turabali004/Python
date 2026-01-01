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
def my_decoraters(func):
      def wrapper(*args, **kwargs):
            print("Before Function")
            result = func(*args, **kwargs)
            print("After Function")
            return result
      return wrapper

@my_decoraters
def Func():
      print("hello world")
Func()
      