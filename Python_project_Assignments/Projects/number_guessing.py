import random

def guess_number():
    """
    This function will guess the number and returns it in how many attempts the user guessed.
    """
    count = 0
    number_to_guess = random.randint(1,100)
    
    while True:
        count += 1
        if count <= 10:
            user_input = int(input("Guess the Number : "))

            if user_input == number_to_guess:
                return f"Congratulations! you guessed it in {count} attempts."
            
            elif user_input > number_to_guess:
                print(f"{user_input} is high! Try Again.")
            
            else:
                print(f"{user_input} is low! Try Again")
        
        else:
            return "Game Over! Better luck next time."

if __name__ == '__main__':
    print(guess_number())