'''
def strong(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact


num=145
sum=0
temp=num
while temp!=0:
    digit=temp%10
    sum+=strong(digit)
    temp//=10
if sum==num:
    print("True")
else:
    print("False")
'''


import math

def strong(num):
    temp=num
    sum=0
    while temp!=0:
        digit=temp%10
        sum=sum+math.factorial(digit)
        temp//=10
    if sum==num:
        return "Strong"
    else:
        return "Not Strong"

num=145
print(strong(num))
    