def slice_and_index(user_input):
    """
    The function takes the input string and prints the sliced and index sting along with reverse of a string
    """

    res = user_input.split(" ")
    i = 0
    for index, word in enumerate(res):
        if len(word) >= 6:
            if index == 0:
                print("First Word :", word[:7])
            
            else:
                print("Amazing part :", word[:7])
    
    print("Reverse of a string :" , user_input[:: -1])

def string_methods(sentence):
    """
    This function takes the input and does the following operations
    1. strip()
    2. Capitalize()
    3. replace()
    4. upper()
    """

    # Strip -> Remove unncessary spaces
    stripped_sentence = sentence.strip()
    print("Removed spaces :", stripped_sentence)

    # Capitalize() -> Capitalizes the first letter of a word/ sentence
    print("After capitalizing the letter : ", stripped_sentence.capitalize())

    # replace() -> Replace the word

    print("After replacing : ", stripped_sentence.replace("World", "Universe"))

    # Upper() -> Uppercase of the senetence

    print("After upper case :", stripped_sentence.upper())

def pallindrome(input1):
    """
    This function takes an argument to check the given word is pallindrome and returns it.
    """
    reverse = input1[::-1]

    if reverse == input1:
        return f"The word {input1} is a pallindrome!"
    else:
        return f"The word {input1} is not a pallindrome!"

if __name__ == '__main__':
    
    print("Executing Task 1 -- String Slicing and Indexing")
    input1 = input("Please enter a string to slice and index to six characters : ")
    slice_and_index(input1)
    
    print("Executing Task 2 -- String Methods")
    string_methods(" Hello, World ")


    print("Executing Task 3 --  check pallindrome")
    user_input  =input("Please enter the word : ")
    print(pallindrome(user_input))