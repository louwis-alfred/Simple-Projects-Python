def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

while True:
    v1 = int(input('Enter first num: '))
    v2 = int(input('Enter second num: '))
    operator = input('Select a operator [add, subtract, multiply]: ').lower().strip()
    
    if operator == 'add':
        result = add(v1,v2)
    elif operator == 'subtract':
        result = subtract(v1,v2)
    elif operator == 'multiply':
        result = multiply(v1,v2)
    else:
        print(f'{operator} is not recognized. Please try again')
    
    print(f'Output: {result}')
        
    while True:
        question = input('Do you want to continue? [yes/no]: ').lower()
        if question in ['yes','no']:
            break
        else:
            print('Please select yes or no only')
            
    if question == 'no':
        break
    
print('See you again!')
    