import sys

print('Enter your name')

while True:
    
    your_name = input('>')
    
    if your_name == 'your name':
        print('Thank you!')
        sys.exit()
    else:
        print('Enter your name')
