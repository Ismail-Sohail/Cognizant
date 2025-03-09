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
    print("Welcome to Recrursive Artistry Program! Choose an option from below")
    print("1. Calculate Factorial")
    print("2. Find Fibonacci")
    print("3. Exit")
    while True:
        user_input = int(input("Choose an Option: "))
        if user_input > 0 and user_input < 4:
            if user_input == 1:
                num = int(input("Please enter a number to find factorial: "))
                print(f"Factorial of a {num} is :", factorial_recursion(num))
                break

            
            elif user_input == 2:
                num = int(input("Please enter a number to find fibonacci: "))
                print(f"fibonacci of a {num} is :", fibonacci(num))
                break
            
            else:
                print("Thank you for playing")
                break
        
        else:
            print("Please choose from the options: ")

