import re

# Function to check if the password is at least 8 characters
def pwordCheck0(pword):
    patterns = r'.{8,}'
    return re.search(patterns,pword)

# Function to check if the password has an upper case letter
def pwordCheck1(pword):
    patterns = r'[A-Z]+'
    return re.search(patterns,pword)

# Function to check if the password has a lower case letter
def pwordCheck2(pword):
    patterns = r'[a-z]+'
    return re.search(patterns,pword)

# Function to check if the password has a number
def pwordCheck3(pword):
    patterns = r'[0-9]+'
    return re.search(patterns,pword)

# Function to check if the password has a symbol (!@#$%^&*)
def pwordCheck4(pword):
    patterns = r'[!@#$%^&*]+'
    return re.search(patterns,pword)

def tryAgain(answer):
    while str.lower(answer)=='y':
        check = input('\nWould you like to try again? (y/n): ')
        if str.lower(check) == 'y' or str.lower(check) == 'n':
            answer = check
            return answer
        else:
            print('Please use either Y for Yes or N for No')

# Main function
if __name__ == "__main__":

    # Loop control for main menu
    answer = 'y'
    while str.lower(answer)=='y':

        # Display password requirements
        print('\nPlease create a strong password.')
        print()
        print('A strong password is defined as one that:\n\
                Is at least eight characters long\n\
                Contains both uppercase and lowercase characters\n\
                Contains one symbol (!@#$%^&*)\n\
                Has at least one digit\n') 

        # Take in password as input
        pword = input('Please input your strong password: ')
        print()

        # Check password for each requirement and store state
        check0 = pwordCheck0(pword)
        check1 = pwordCheck1(pword)
        check2 = pwordCheck2(pword)
        check3 = pwordCheck3(pword)
        check4 = pwordCheck4(pword)

        # Print any password requirements not met
        if not check0:
            print('Password is not at least eight characters')
        if not check1:
            print('Password does not have an upper case letter')
        if not check2:
            print('Password does not have a lower case letter')
        if not check3:
            print('Password does not have a number')
        if not check4:
            print('Password does not have a symbol (!@#$%^&*)')
        if check0 and check1 and check2 and check3 and check4:
            print('Password meets all requirements.')

        # Uses tryAgain function to change loop control flag and exit program or restart main menu loop
        answer = tryAgain(answer)

