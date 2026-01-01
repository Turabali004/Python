# number = int(input("Provide me a age: "))

# if number is None:
#       print("Please enter a number")
# elif number <= 18:
#       print("Teenager")
# elif number > 18 or number < 24:
#       print("Younger")
# else:
#       print("not Teen Age")


# def even_or_odd(n):
#     if not isinstance(n, int):
#         return "invalid"
#     return "even" if n % 2 == 0 else "odd"

# print(even_or_odd(5))


# Problem 5: Shipping cost calculator
# - Task: Implement shipping_cost(weight, country):
# - If weight <= 0, return "invalid".
# - Base cost: PK → 200, US → 1000, UK → 800, else 1500.
# - Add surcharge: +100 if weight > 5, +300 if weight > 20.
# - Return total as integer.


def even_or_odd(weight, country):
    if not isinstance(weight, (int, float)) or weight <= 0:
        return "invalid"
    base = {
        "pakistan": 200,
        "usa": 1000,
        "uk": 800,
    }.get(
        country, 15000
    )
    print(base, country)
    surCharge = 0
    if weight > 5:
      surCharge = 100
    elif weight > 20:
      surCharge = 300
    return surCharge + base    




print(even_or_odd(22, "asdf"))
