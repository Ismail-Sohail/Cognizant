
def python_exception():
    
    try:
        num = int(input("Enter the value : "))
        result = 100 / num

    except ValueError:
        print("Invalid input! Please enter a valid number.")
    
    except ZeroDivisionError:
        print("Enter number greater than zero")
    
    else:
        print("Result", result)

def handle_exceptions():
    # Handle IndexError by accessing an invalid index in a list
    try:
        my_list = [1, 2, 3]
        print(my_list[5])  # Index 5 is invalid, the list has only 3 elements
    except IndexError as e:
        print(f"IndexError occurred: {e}")
        print("Explanation: Index 5 is out of range for this list.")

    # Handle KeyError by trying to access a non-existent key in a dictionary
    try:
        my_dict = {"name": "Alice", "age": 25}
        print(my_dict["address"])  # "address" is not a key in the dictionary
    except KeyError as e:
        print(f"KeyError occurred: {e}")
        print("Explanation: 'address' is not a key in the dictionary.")

    # Handle TypeError by adding a string and an integer
    try:
        result = "Hello" + 5  # You cannot add a string and an integer directly
    except TypeError as e:
        print(f"TypeError occurred: {e}")
        print("Explanation: You cannot add a string and an integer directly. This raises a TypeError.")


def Full_exception():
    
    try:
        num1 = int(input("Enter the value : "))
        num2 = int(input("Enter the value :"))
        result = num1 / num2

    except ValueError:
        print("Invalid input! Please enter a valid number.")
    
    except ZeroDivisionError:
        print("Enter number greater than zero")
    
    else:
        print("Result", result)
    
    finally:
        print("This block always executes.")


if __name__ == '__main__':
    
    print("Executing Task 1 -- Understanding Python Exceptions")
    python_exception()
    
    print("\n")
    print("Executing Task 2 -- Types of Exception")
    handle_exceptions()

    print("\n")
    print("Executing Task 3 --  Working with Exceptions")
    Full_exception()
    