# Homerowk 1.2  Dimitar Dimitrov

a = float(input('a = '))
b = float(input('b = '))
d= (a*b)/2
print('The area of right triangle with sides a = {}, b = {} is {}'.format(a, b, d))

def triangle(a,b):
    y = (a*b)/2
    return y
res =  triangle(a,b)
print('The area of right triangle with sides a = {}, b = {} is {}'.format(a, b, res))
