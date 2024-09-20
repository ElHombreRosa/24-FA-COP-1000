#Code From Professor Video

def checkInput(input):
#Decision Structures
    if(not input.isnumeric()):
        return f'{input} is not numeric. Please try again'

    if(int(response) > 10 or int(response) < 1):
        return f'{input} is out of bounds. Please try again'

    #happy path
    return f'The number is {input}'

#Iterative Statements inf loop 
while (True):
    response = input("Pleasen enter a number between 1 and 10: ")
    print(checkInput(response))