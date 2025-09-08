#Reverse Words in a Sentence
def reverse_sen(s):
    s1=s.split(' ')
    rev = s1[::-1]
    return ' '.join(rev)

s="Hello world this is Django"
print(reverse_sen(s))


#Factorial of a Number (Using Recursion)

'''def factorial(n):
    if n==0 and n==1:
        return 1
    return n* factorial(n-1)

n=5
print(factorial(n))'''



#Check if a String is a Palindrome(Ignore case and spaces in the input.)

'''def palindrome(s):
    
    s1=s.lower().split(' ')

    rev_s=''
    for i in s1:
        rev_s+=i
    # if rev_s==rev_s[::-1]:
    #     return True
    # else:
    #     return False
    return rev_s==rev_s[::-1]
    
s="Race car"
print(palindrome(s))'''


'''def palindrome(s):
    cle = s.replace(' ','').lower()
    return cle == cle[::-1]

s="Race car"
print(palindrome(s))'''



#Find the Second Largest Number in a List

'''def second_largest(num):
    num =sorted(set(num))
    return num[-2]

num = [4, 1, 2, 7, 7, 5]
print(second_largest(num))'''



#Merge Two Sorted Lists(without using the built-in sort() function)
'''
def sort_two_lists(l1,l2):
    l=l1+l2
    l.sort()
    return l
    

l1,l2=[1, 3, 5], [2, 4, 6]
print(sort_two_lists(l1,l2))'''


'''
def sort_two_lists(l1,l2):
    res=[]
    i=j=0

    while i<len(l1) and j <len(l2):
        if l1[i]<l2[j]:
            res.append(l1[i])
            i+=1
        else:
            res.append(l2[j])
            j+=1
    
    while i <len(l1):
        res.append(l1[i])
        i+=1

    while j<len(l2):
        res.append(l2[j])
        j+=1
    return res

l1,l2=[1, 3, 5], [2, 4, 6]
print(sort_two_lists(l1,l2))
'''


#Find the Common Elements in Two Lists

'''def common_element(l1,l2):
    l3=[]
    for i in l1:
        if i in l2 and i not in l3:
            l3.append(i)
    return l3

l1,l2= [1, 2, 2, 3, 4], [2, 3, 5]
print(common_element(l1,l2))
'''


#Implement a Stack using a Python Class

'''class Stack:
    
    def __init__(self):
    
        self.stack=[]

    def push(self,item):
        self.stack.append(item)
        
        return self.stack
    
    
    
    def pop(self):
        if self.is_empty():
            return "stack is empty"
        return self.stack.pop()
        
    
    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack)==0
    
   
        

s1=Stack()

print(s1.push(10))   
print(s1.push(20)) 
print(s1.peek())
'''



#Remove Duplicates From a List Without Using Set

'''def remove_duplicates(l):
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
    return l1

l=[1, 2, 2, 3, 1, 4]
print(remove_duplicates(l))'''


#Count the Number of Vowels in a String

'''def count_vowls(s):
    s1='AEIOUaeiou'
    count =0
    for i in s:
        if i in s1:
            count+=1
    return count

s= "Hello World"
print(count_vowls(s))
'''