def rotate(l,k):
    k=k%len(l)
    l[:]=l[-k:]+l[:-k]
    return l

l=[3,5,4,7,9,8]
k=3
print(rotate(l,k))