#brute force approch

'''
n=5
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
'''



# using recursion

'''
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
    

n=5
print(fact(n))
'''























# num= int(input("enter number: "))
# fact =1
# for i in range(2,num+1):
#     fact *=i
# print (fact)




# def factorial(num):
#     fact =1
#     for i in range(2,num+1):
#         fact *= i
#     return fact

# num = int(input("enter a number :"))
# print(factorial(num))




# def fact(num):
#     if num==1:
#         return 1
#     else:
#         return num * fact(num-1)
# num=5
# print(fact(num))




# def febbinoci(num):
#     if num<=1:
#         return num
#     return febbinoci(num-1)+febbinoci(num-2)

# num=int(input("enter a number:"))
# for i in range(num):
#     print(febbinoci(i),end=' ')



# def reverse(s):
#     s1=''
#     for i in s:
#         s1=i+s1
#     return s1
# s="sivanji"
# print(reverse(s))


def reverse(s):
    s1=''
    for i in range(len(s)-1,-1,-1):
        s1+=s[i]
    return "palindrome" if s==s1 else  "notpalidrome"
s="sivanji"
print(reverse(s))