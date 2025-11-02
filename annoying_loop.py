import sys

print('Enter your name')

while True:
    
    your_name = input('>')
    
    if your_name == 'your name':
        sys.exit()
    else:
        print('Enter your name')
