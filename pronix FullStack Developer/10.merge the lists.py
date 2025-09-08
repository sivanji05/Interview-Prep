l1=[3,5,4,7,6,8,4]
l2=[2,3,1,5,4,7,9]
l3=[]
for i in l1+l2:
    if i not in l3:
        l3.append(i)
print(l3)


# 2nd method
l3 = list(dict.fromkeys(l1 + l2))
print(l3)