# Homerowk 1.1  Dimitar Dimitrov

int_var_from_user = int(input('Input a digit:'))
print('Your digits is: {}'.format(int_var_from_user))
print('{} multiplied by two equals {}'.format(int_var_from_user, int_var_from_user*2))

def mult(a):
    y = a*2
    return y
res = mult(int_var_from_user)
print('{} multiplied by two equals {}'.format(int_var_from_user, res))
