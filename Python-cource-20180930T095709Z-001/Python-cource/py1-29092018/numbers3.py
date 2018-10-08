a = b = [1,2,3]
print(a,b)

a[1] = 4
print(a,b)

print(a is b) # same object in memory
print(b is a)

a = [1,2,3]
b = [1,2,3]

print(a is b) # same object in memory
print(b is a)

a,b,c = 1,2,3
print(a,b,c)

a,b,c = [1,2,3]
print(a,b,c)

[a,b,c] = (1,2,3)
print(a,b,c)

a,b, *c = 1,2,3,4,5,6,6,7,8,9,10
print(a,b,c)