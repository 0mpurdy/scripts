# Simple menu system

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def printMenu(menu):
    i = 0
    for item in menu:
        print(str(i) + ' - ' + item)
        i += 1

def getMenuChoice(menu):
    print("\nPlease select an option from the menu:\n")
    printMenu(menu)
    choice = input('-->')
    return num(choice)

def close():
    print('closing')
    
def printHello():
    print('Hello')

def greet():
    print('Hello Person')
    

print("Hello World!")

menu = ['Close', 'Print hello', 'Greet']

# map the inputs to the function blocks
options = {0: close,
           1: printHello,
           2: greet,
}

options[getMenuChoice(menu)]()
