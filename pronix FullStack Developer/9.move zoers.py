def moveZeros(n):
    left=0
    for right in range(len(n)):
        if n[right]!=0:
            n[right],n[left]=n[left],n[right]
            left+=1
    return n

n=[1,3,0,2,3,2,0,0,5,3]

print(moveZeros(n))

