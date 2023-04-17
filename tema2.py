l1 = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
l2 = l1.copy()
l2.sort()
print(l2)
l2.sort(reverse=True)
print(l2)
print(l1[0::2])
print(l1[1::2])
l2.clear()
for i in l1:
    if i % 3 == 0:
        l2.append(i)
print(l2)
