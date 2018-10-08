aList = ['123', 'zara', 'abc', 'xyz']
aList.sort()
print("List : ", aList)

aList.sort(reverse=True)
print("List sorted in reverse order: ", aList)

aList.sort(key=len)
print("List sorted by len: ", aList)

aListNum = [-12,1,312,32.54]
aListNum.sort()
print("Numeric List : ", aListNum)

aListNum.sort(reverse=True)
print("Numeric List sorted in reverse order: ", aListNum)