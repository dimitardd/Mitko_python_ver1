# Homework 2.4 Dimitar Dimitrov

y = str(input('Please insert some string: '))
z = len(str(y))
x = (len(str(y)) - 2)
a = str(y)[x:]

if z <= 2:
    print('Empty String')
else:
    print(a)
