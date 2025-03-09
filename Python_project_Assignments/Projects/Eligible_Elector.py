
def voter_eligibility(age):
    """
    This function takes the age as an arguments and returns whether the person is eligible to vote. 
    """

    if age > 0:
        if age > 18:
            return "Congratulations! You are eligible to vote. Go make a difference"
        
        else:
            return f"Oops! You're not eligible yet, But hey, only {18-age} more years to go"
    
    else:
        return "Please enter the valid age"



if __name__ == '__main__':
    
    age = int(input("How old are you ? "))
    print(voter_eligibility(age))