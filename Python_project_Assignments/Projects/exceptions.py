def check_valid_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter the valid integer number: ")


def calculator(choice):
    """
    Function takes 2 arguments and returns the addition of 2 numbers
    """

    try:
        num1 = check_valid_input("Please enter first number: ")
        num2 = check_valid_input("Please enter second number: ")
        if choice == 1: res = num1 + num2
        elif choice == 2: res = num1 - num2
        elif choice == 3: res = num1 * num2
        else: res = num1 / num2
    
    except ZeroDivisionError as e:
        print(f"{e} *** cannot divide by zero, please enter number greater than zero ****")
    
    else:
        return f"The answer is: {res}"

def menu_operations():
    
    while True:
        print("********* Welcome to Error Free Calculator ********")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            choice = int(input("Choose a operation to perform "))
        
        except ValueError:
            print("Please enter a valid number between 1 and 5")

        else:
            if choice <= 0 or choice > 5:
                print("Please choose a number between 1 and 5") 
            
            elif choice == 5:
                print("Thank you for exploring the Calculator. See you soon!")
                break
            else:
                print(calculator(choice=choice)) 


if __name__ == '__main__':
    menu_operations()

    



