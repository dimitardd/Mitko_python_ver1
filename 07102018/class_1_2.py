# work in class Dimitar Dimitrov

import random

list_10 = random.sample(range(0, 100), 10)

a = int(input('Please insert number from 0 ro 100 : '))

# if a not in list_10 and a < 100:
#     print('Not found {} in list {}'.format(a, list_10))
# elif a in list_10:
#     print('Found {} in list {}'.format(a, list_10))
# else:
#     print('Not in range 0 to 100')

def check_l(a):
    if a not in list_10 and a < 100:
        result = ('Not found {} in list {}'.format(a, list_10))
    elif a in list_10:
        result = ('Found {} in list {}'.format(a, list_10))
    else:
        result = ('Not in range 0 to 100')
    return result

res = check_l(a)
print(res)