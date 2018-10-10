# Homework 2.5 Dimitar Dimitrov
a = int(input('Please insert list of numbers: '))
if a > 0:
#    x = list(map(int, str(a)))
    x = list(map(int, a))
    b = sum(x)
    print(b, ' is sum of ', a)
else:
    print('The number is not  positive number')