# Homework 2.6 Dimitar Dimitrov

a = input('Please insert string:')
b = a.isdigit()

if b == True:
    print('Yes, {} can be represented as an integer'. format(a))
else:
    print('This is not an integer')
