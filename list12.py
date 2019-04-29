#list
l1=[2,3,4,5,6,66,7,7,56,7,7,7]
print("index of 66",l1.index(66))
#print(type(l1))
#print(l1[5])
#print(l1[8])
maxi = max(l1)
#print(maxi)
mini = min(l1)
#print(mini)
#pop
print('List before poping',l1)
l1.pop()
print('list after poping',l1)
l1.append(34)
print(l1)
l1.remove(66)

print(l1)
print(l1.count(7))
#print(l1.index(66))
