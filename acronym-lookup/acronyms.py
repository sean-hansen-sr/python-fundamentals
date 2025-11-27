def find_acronym():
    look_up = input('What software acronym would you like to look up?\n')

    found = False

    try:
        with open('software_acronyms.txt') as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print("The acronym file does not exist.")
        return
    
    if not found:
        print("Acronym not found.")

def add_acronym():
    acronym = input('Enter the acronym you want to add:\n')
    definition = input('Enter the definition for the acronym:\n')

    with open('software_acronyms.txt', 'a') as file:
        file.write(f'{acronym} - {definition}\n')

if __name__ == '__main__':
    choice = input('Would you like to find (F) an acronym or (A) add a new one?\n')
    if choice.upper() == 'F':
        find_acronym()
    elif choice.upper() == 'A':
        add_acronym()
