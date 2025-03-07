
def Intro():
    """
    Function returns the Intro of the given person.
    """
    name = 'Ismail'
    age = 26
    height = 5.4

    return f"Hey there, My name is {name}! I'm {age} years old and {height} feet tall"

def operators(num1, num2):
    """
    This function takes the two numbers, compute & prints the Addition, Subtraction, Multiplication, & Division of 2 numbers
    """
    # Addition
    print(f"The sum of {num1} and {num2} is : ", num1 + num2 )
    # Subtraction
    print(f"The difference of {num1} and {num2} is : ", num1 - num2 )
    # Multiplication
    print(f"The multiplication of {num1} and {num2} is : ", num1 * num2 )
    # Division
    print(f"The Division of {num1} and {num2} is : ", num1 // num2 )

def check_number(user_input):

    """
    This function takes user input and returns the number is negative, positive or zero
    """

    if user_input > 0:
        return "Given number is Positive. Awesome!"

    elif user_input < 0:
        return "The number is Negative. Better luck next time!"

    else:
        return "Zero it is. perfect balance"

if __name__ == '__main__':
    print("Executing Task 1 -- Variables: Your First Python Intro")
    print(Intro())
    print("Executing Task 2 -- Operators: Playing with Numbers")
    operators(10, 2)
    print("Executing Task 3 -- Conditional Statements: The Number Checker")
    user_input  = int(input("Please share the number : "))
    print(check_number(user_input))
