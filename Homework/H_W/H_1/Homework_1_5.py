# Homework 1.5 Dimitar Dimitrov
import random
list_10 = random.sample(range(0, 100), 10)
#print('List is : {}'.format(list_10))
a = int(input('Please insert number from 0 ro 100 : '))
if a in list_10:
    print('Found {} in list {}'. format(a, list_10))
else:
    print('Not found {} in list {}'. format(a, list_10))