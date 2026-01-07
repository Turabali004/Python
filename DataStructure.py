# Lists
my_list = ["apple", "banana", "cherry"]
# print(my_list)

# for items in my_list:
#     print(items)

# my_numbers = [1, 2, 3, 4, 5]
# for numbers in my_numbers:
#     for number in range(numbers, 5+1):
#         print(number*number)
    
#     break;


def sumFunc(*numbers): 
    return sum(numbers)

# print(sumFunc(1, 2, 3, 4, 5))


# def multiplValueWithKey(**kwargs):
#     # return kwargs
#     # for key, value in 
#     # print(kwargs.items())
#     for key, value in kwargs.items():
#         return (f"{key} is {value}")

# values = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }

# print(multiplValueWithKey(**values))


# Dictionary creation (key-value pairs)
person = {
    "name": "John",
    "age": 25,
    "city": "NYC"
}

# Dictionary operations
# print(person["name"])           # Access value
# print(person.get("age"))        # Get with default
person["email"] = "j@ex.com" 
# print(person)
# Add/Update
# del person["city"]              # Delete key
# person.pop("age")               # Remove and return

# Dictionary methods
# print(person.keys())            # All keys
# print(person.values())          # All values
# print(person.items())           # All key-value pairs

# Dictionary iteration
for key, value in person.items():
    print(key, value)

# Dictionary comprehension
# squares = {x: x**2 for x in range(5)}
# squares = {x*2 for x in range(5)}
# print(squares)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}