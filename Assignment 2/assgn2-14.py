length = low = up = dig = False

pas = input('Enter the Password: ')

if len(pas)>= 8:
    length = True
    
    for let in pas:
        if let.islower():
            low = True
        elif let.isupper():
            up = True
        elif let.isdigit():
            dig = True


if (length and low and up and dig):
    print('This is a valid password.')
else:
    print('This password is not valid.')
