# febbanoci series

# def febacoi(n):
#     n1=0
#     n2=1

#     for i in range(2,n):
#         n3=n1+n2
#         n1=n2
#         n2=n3
#         print(n3, end=" ")
#     return

# n=int(input('Enter the number:'))
# print(febacoi(n))



#using burte force 

# n=5
# n1=0
# n2=1
# for i in range(2,n):
#     n3=n1+n2
#     n1=n2
#     n2=n3
#     print(n3)

 
# with recurssion

def feb(n):
    if n<=1:
        return n    
    else:
        return feb(n-1)+feb(n-2)
n=5
for i in range(n):
    print(feb(i), end=" ")
    




# Brtue force approch

# num = 5
# n1, n2 = 0, 1
# print("Fibonacci Series:", n1, n2, end=" ")
# for i in range(2, num):
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     print(n3, end=" ")







