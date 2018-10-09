# Homework 2.2 Dimitar Dimitrov

y = int(input('Please insert year: '))

def century(y):
    a = (int(len(str(y))) - 2)
    first_d = int(str(y)[:a])
    check_zero = int(str(y)[2:])
    if check_zero == 00:
        print(y, ' is in ', (first_d))
    else:
        print(y, ' is in', (first_d+1), 'Century')
    return

if 1 <= y <= 100:
    print(y, ' is in 1st Century')
else:
    century(y)