
def lists_functions(fruits):
    """
    This function takes the list and performs the some of the common list operations
    """

    print("Original list of fruits : ", fruits)

    fruits.append("fig")
    print("After adding a fruit : ", fruits)

    fruits.remove('apple')
    print("After removing a fruit : ", fruits)

    fruits = fruits.reverse()
    print("Reverse of a fruits list : ", fruits)


def dictionary_functions(info_dict):
    """
    This function takes the input as a dictionary and performs the dictionary operations

    """
    info_dict['favourite color'] = "Blue" # Adds the new key and value
    info_dict['city'] = 'Toronto' # Update the city to Toronto

    #Loops over the dictionary and prints the dict values
    for key, value in info_dict.items():
        print(f"{key}: {value}")

def tuple_functions(movies):
    """
    This function takes the input as a tuple and performs the tuple operations

    """

    try:
        movies[0] = 'Open Heimer'
    
    except TypeError:
        print("OOPS! Tuples are immutable")
    
    print("Length of the tuple is : ", len(movies)) # prints the length of the tuple


if __name__ == '__main__':
    
    print("Executing Task 1 -- Working with Lists")
    fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    lists_functions(fruits)

    print("\n")
    print("Executing Task 2 -- Working with Dictionary")
    info_dict = {"name": "Ismail", "age": 26, "City": "Ontario"}
    dictionary_functions(info_dict)

    print("\n")
    print("Executing Task 3 --  Working with Tuple")
    movies = ('Inception', 'Bohemian Rhapsody', '1984')
    tuple_functions(movies)
    