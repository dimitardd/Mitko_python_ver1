# Homework 2.10 Dimitar Dimitrov

a = (input('Tape word: '))
n = 10
print(type(a))
print(a)
print(len(a), 'is len of word')


while n > 0:
    y = (input('Tape the word '))
    if y in a:
        print(y)
        a = a.replace(y, '')
        print(a)
    else:
        print('Sorry {} is not in the word'. format(y))
    n -= 1
    print('You have {} more tries'. format(n))

print('No more options')
