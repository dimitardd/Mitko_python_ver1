list1 = ['physics', 'chemistry', 1997, 2000]
print(list1)

del list1[2]

print("After deleting value at index 2 : ")
print(list1)

list1.remove(list1[2])

print("After deleting value at index 2 : ")
print(list1)

print("Len of the list " + str(len(list1)))
print("Len of the list " + len(list1).__str__())
print("Len of the list {}".format(len(list1)))

list2 = ["mathematics", "chemistry"]

result_list = list1 + list2

print(result_list)

test_list = ["Yeaa!",90]*3
print(test_list)

print("chemistry" in result_list)

print(end="\n")
print("Some books",end="\n------------\n")

for y in result_list:
   print(y)