list1 = [33,25,65,75,23]
list2 = [34,64,78,49,22]
list3 = list1 + list2
odd = []
even = []
for i in list3:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
        list3 = even+odd
even.sort()
odd.sort()
print(even)
print(odd)
print(list3)