
def greet_user(name):
    return f"Hello, {name}! Welcome aboard."

def add_numbers(num1, num2):
    res = num1 + num2
    return f"The sum of {num1} and {num2} is : {res}"

def describe_pet(pet_name, animal_type = 'Dog'):
    return f" I have a {animal_type} named {pet_name}."

def make_sandwich(*ingredients):
    print("Your sandwich contains the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")


def factorial_recursion(num):
    if num == 1:
        return 1
    
    res = num * factorial_recursion(num - 1)

    return res

def fibonacci(num):
    if num == 0:
        return 0
    
    if num == 1:
        return 1
    
    res = fibonacci(num -1) + fibonacci(num - 2)

    return res


if __name__ == '__main__':
    
    print("Executing Task 1 -- Writing Functions")
    print(greet_user("Ismail"))
    print(add_numbers(10,2))
    
    print("Executing Task 2 -- Using Defalut Parameters")
    print(describe_pet("Buddy"))

    print("Executing Task 3 --  Find the Factorial")
    make_sandwich("bread", "cheese", "lettuce", "tomato", "ham")

    print("Executing Task 4 --  Understanding recursion")

    print("Factorial of a number 5 is : ", factorial_recursion(5))
    print("Fibonacci of a number 6 is : ", fibonacci(6))
