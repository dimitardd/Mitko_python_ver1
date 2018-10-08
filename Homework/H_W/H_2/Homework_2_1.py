# Homework 2.1 Dimitar Dimitrov

while True:
    try:
        d = int(input('Please insert number : '))
        break
    except ValueError:
        print('     Please insert digit!!!      ')

a=d//2
if d > 0:
    for y in range(2,a):
        if (d % y) == 0:
            print(d, 'is not a prime number')
            print(y, 'time', d//y, 'is', d)
            break
    else:
        print(d,' is a prime number')
        print(range(2, a))
else:
    print(d, 'is not a prime number')