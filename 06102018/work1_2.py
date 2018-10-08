# 1.2 Dimitar Dimitrov

c = float(input('Temperature in Celsius = '))
f = (c*1.8) + 32
print('{} degrees Celsius in Fahrenheit is {}'.format(c, f))

def ctof(a):
    "Cesius to Farenheit"
    print((a*1.8) +32)
    return

ctof(c)

def ctof_1(a):
    "Cesius to Farenheit"
    b = (a*1.8) + 32
    return b

resultat = ctof_1(c)
print('Print of ctof_1 is : {}'.format(resultat))