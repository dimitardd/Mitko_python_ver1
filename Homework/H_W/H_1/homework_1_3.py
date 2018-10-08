# Homework 1.3 Dimitar Dimitrov
max_d = []
# a = input('Value for index 0: ')
# b = input('Value for index 1: ')
# c = input('Value for index 2: ')
# max_d.append(a)
# max_d.append(b)
# max_d.append(c)
# print(max_d)

max_d.insert(0, input('Value for index 0: '))
max_d.insert(1, input('Value for index 1: '))
max_d.insert(2, input('Value for index 2: '))
print(max_d)
print(sorted(max_d, key=int))
print(sorted(max_d)[2])
print('The maximum of {}, {} and {} is {}'.format(max_d[0], max_d[1], max_d[2], sorted(max_d, key=int)[2]))



