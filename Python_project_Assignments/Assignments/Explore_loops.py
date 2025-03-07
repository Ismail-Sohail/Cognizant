
def count_reverse(user_input):
    """
    Function returns the reverse count of a number.
    """
    while user_input > 0:
        print(user_input, end = " ")
        user_input -= 1
    
    print("Blast off!")

def multiplication_table(num1):
    """
    This function takes a number and prints the multiplication of a number
    """
    for i in range(1,11):
        print(f"{num1} X {i} = ", num1 * i)

def factorial(user_input):

    """
    This function takes user input and returns the factorial of a number
    """

    res = user_input
    num = user_input - 1
    while num > 0:
        res = res* num
        num -= 1
    return res

if __name__ == '__main__':
    
    print("Executing Task 1 -- Counting Down with Loops")
    input1 = int(input("Please share a number : "))
    count_reverse(input1)
    
    print("Executing Task 2 -- Multiplication table")
    input2 = int(input("Enter a number : "))
    multiplication_table(input2)

    print("Executing Task 3 --  Find the Factorial")
    user_input  = int(input("Please enter the number : "))
    print(factorial(user_input))
    