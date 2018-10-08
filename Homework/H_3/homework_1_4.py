# Homework 1.3 Dimitar Dimitrov

c = float(input('Temperature in Celsius = '))
f = (c*1.8) + 32
print('{} degrees Celsius in Fahrenheit is {}'.format(c, f))

ctof = lambda c: (c*1.8) + 32

print(c, ' degrees Celsius in Fahrenheit is ', ctof(c))