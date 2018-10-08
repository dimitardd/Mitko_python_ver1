# Homework 2.2 Dimitar Dimitrov
# if d = 1000000000
# 42sec with optimization
# 86sec without optimization

d = int(input('Please insert number : '))
r = []
#a = (d//2)+1
if d > 0:
    for y in range(1,d+1):
        if (d % y) == 0:
            r.append(y)
#            r.extend(str(y))
#            print(type(y))
            continue
#r.append(d)
print(r)