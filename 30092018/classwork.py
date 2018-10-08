print ('Hello {0}! How are you today {1}'.format ('Dimitar','Mr. Dimitrov'))
print (f'Hello {"Dimitar"}! How are you today {"Mr. Dimitrov"}')

# print test
a = 'dimitar'
print(a.capitalize())
print(a.upper())

a = 'dimitar hristov dimitrov'

print(a.capitalize()) # vdiga samo pyrvta bukva ot stringa
print(a.capitalize())
print(a.title())  # vdiga vsqka pyrva bukva ot vsqka duma
print(a.upper())
print(a.find('dimitrov')) # ot koi index zapochva dadeniq string, 0 e nachalniqt string

# multiline string

x = '''
Multi
Line
Test
'''
print(x)

str = 'This is string exapmple !!!!!'
suffix='!!!'
print(str.endswith(suffix))

str = "This IS TEst UPER and lower"
print(str.swapcase())

# Kogato broim sys opciq 'len' kursura trqbva da e pred simvola i se broi
