# Global List
list = ['toward', 18597, 'clear', 'last', 'task', 'family', 'leader', 'say', 'indicate', 'military', 'hit', 'available', 'equal', 'find', ['purple', 'needle', 7895, 'clearly'], 'forty', 'inside', ['during', 'very', 'pilot', 'region'], 'seems', 'discover']

# Navigation functions to display the main menu and global list and to restart after each menu option is completed
def showMenu():
    print()
    print("\n Please select from the following choices:")
    print('1   Display the list')
    print('2   Add an item to the list at the end')
    print('3   Add an item to the list at the start')
    print('4   Add an item to the list in a certain position')
    print('5   Delete an item from the list by name')
    print('6   Delete the first item')
    print('7   Delete the last item')
    print('8   Delete an item by position')
    print('9   Show the first N items')
    print('10  Show the last N items')
    print('11  Check if an item is in the list')
    print('12  Add a cat named Eric to the list')
    print('0   Exit the program')

def displayList():
    print()
    print(list)

def tryAgain(answer):
    while str.lower(answer)=='y':
        check = input('\nWould you like to try again? (y/n): ')
        if str.lower(check) == 'y' or str.lower(check) == 'n':
            answer = check
            return answer
        else:
            print('Please use either Y for Yes or N for No')

# The Functions for each number option on the main menu
def addEndList():
    item = input('Please specify item (default: Ernst Bekkering): ') or 'Ernst Bekkering'
    list.append(item)
    displayList()

def addStartList():
    item = input('Please specify item (default: Ernst Bekkering): ') or 'Ernst Bekkering'
    list.insert(0, item)
    displayList()

def addPosList():
    item = input('Please specify item (default: Ernst Bekkering): ') or 'Ernst Bekkering'
    while True:
        try:
            pos = int(input('At which position? '))
            if pos == len(list)+1:
                list.append(item)
                break
            elif pos > 0 and pos <= len(list):
                list.insert(pos-1, item)
                break
            else:
                print(f'Please enter an integer between 1 and {1+len(list)}\n')
        except:
            print(f'Please enter an integer between 1 and {1+len(list)}\n')
    displayList()

def delNameList():
    item = input('Please specify item (default: Ernst Bekkering): ') or 'Ernst Bekkering'
    if item.isdecimal() == True:
        item=int(item)
    if item in list:
        list.remove(item)
    else:
        print('That item is not in the list\n') 
    displayList()

def delStartList():
    if len(list) > 0:
        del list[0]
    else:
        print("The list is empty, try putting something in it first!\n")
    displayList()

def delEndList():
    if len(list) > 0:
        del list[-1]
    else:
        print("The list is empty, try putting something in it first!\n")
    displayList()

def delPosList():
    if len(list) > 0:
        while True:
                try:
                    pos = int(input('At which position? '))
                    if pos > 0 and pos <= len(list):
                        del list[pos-1]
                        break
                    else:
                        print(f'Please enter an integer between 1 and {len(list)}\n')
                except:
                    print(f'Please enter an integer between 1 and {len(list)}\n')
    else:
        print("The list is empty, try putting something in it first!\n")
    displayList()

def showFirstList():
    if len(list) > 0:
        while True:
                try:
                    pos = int(input('How many items? '))
                    if pos > 0 and pos <= len(list):
                        print(list[:pos])
                        break
                    else:
                        print(f'Please enter an integer between 1 and {len(list)}\n')
                except:
                    print(f'Please enter an integer between 1 and {len(list)}\n')
    else:
        print("The list is empty, try putting something in it first!\n")
    displayList()

def showLastList():
    if len(list) > 0:
        while True:
                try:
                    pos = int(input('How many items? '))
                    if pos > 0 and pos <= len(list):
                        print(list[-pos:])
                        break
                    else:
                        print(f'Please enter an integer between 1 and {len(list)}\n')
                except:
                    print(f'Please enter an integer between 1 and {len(list)}\n')
    else:
        print("The list is empty, try putting something in it first!\n")
    displayList()

def showNameList():
    item = input('Please specify item (default: Ernst Bekkering): ') or 'Ernst Bekkering'
    print(f'\n' ''' '{item}' is in the list: {item in list}''')
    displayList()
    

def addEricList():
    while True:
        try:
            pos = int(input('At which position? '))
            if pos == len(list)+1:
                list.append('a cat named Eric')
                break
            elif pos > 0 and pos <= len(list):
                list.insert(pos-1, 'a cat named Eric')
                break
            else:
                print(f'Please enter an integer between 1 and {1+len(list)}\n')
        except:
            print(f'Please enter an integer between 1 and {1+len(list)}\n')
    displayList()

# Main function
if __name__ == "__main__":

    # Loop control for main menu
    answer = 'y'
    while str.lower(answer)=='y':

        # Displays main menu and links options to each function
        showMenu()
        try:
            choice = int(input('\n Your choice: '))
            print()
            if choice == 1:
                displayList()

            elif choice == 2:
                addEndList()

            elif choice == 3:
                addStartList()

            elif choice == 4:
                addPosList()

            elif choice == 5:
                delNameList()

            elif choice == 6:
                delStartList()

            elif choice == 7:
                delEndList()

            elif choice == 8:
                delPosList()

            elif choice == 9:
                showFirstList()

            elif choice == 10:
                showLastList()

            elif choice == 11:
                showNameList()

            elif choice == 12:
                addEricList()

            elif choice == 0:
                break

            else:
                print('That is not a valid choice\n')
        except:
            print('That is not a valid choice\n')
        
        # Uses tryAgain function to change loop control flag and exit program or restart main menu loop
        answer = tryAgain(answer)


        

