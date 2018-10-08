# Homework 1.3 Dimitar Dimitrov
max_d = []

max_d.insert(0, input('Value for index 0: '))
max_d.insert(1, input('Value for index 1: '))
max_d.insert(2, input('Value for index 2: '))
print(max_d)
print(sorted(max_d, key=int))
print(sorted(max_d)[2])

def sortirane(a):
    y = sorted(a, key=int)
    return y
res = sortirane(max_d)

print(res)