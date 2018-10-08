# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list
# random = [(2, 2), (3, 4), (4, 1), (1, 3)]

random = [('Anthony', 'Johnson'), ('Peter', 'Smith'), ('George', 'Tason'), ('Elon', 'Musk')]

# sort list with key
random.sort(key=takeSecond)

# print list
print('Sorted list:', random)


