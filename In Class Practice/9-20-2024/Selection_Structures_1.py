def checkInput(input):
    if(not input.isnumeric()):
        return f'{input} is not numeric. Please try again. '
    elif (int(input) > 10 or int(input) < 1):
        return f'{input} is out of bounds. Please try again. '
    else:
        return f'The number is {input}' 
    
#Iterative Statements

#Decision Structures
response = input("Please enter a number between 1 and 10: ")
print(checkInput(response))
