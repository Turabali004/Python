import random


while True:
    choice = input("Roll the dice? (y/n): ")
    if choice == "y" or choice == "Y":
        Num1 = random.randint(1, 88)
        Num2 = random.randint(1, 88)
        print(f"You rolled a {Num1} and a {Num2}")
        
    elif choice == "n" or choice == "N":
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice. Please try again.") 