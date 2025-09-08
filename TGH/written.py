# Write a program to print a pattern of numbers in Python
# The pattern should have alternating rows of increasing and decreasing numbers, like this:
'''rows = 5
num = 1

for i in range(1, rows + 1):
    row = []

    if i % 2 != 0:
        # Odd row: Increasing order
        for _ in range(i):
            row.append(num)
            num += 1
    else:
        # Even row: Decreasing order
        temp = []
        for _ in range(i):
            temp.append(num)
            num += 1
        row = temp[::-1]  # reverse for decreasing

    print(" ".join(str(x) for x in row))'''



# Output:
# 1
# 3 2
# 4 5 6
# 10 9 8 7
# 11 12 13 14 15








# write program to convert roman numerals to integers in python

'''def roman_to_int(s: str) -> int:
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in s:
        value = roman_numerals[char]
        
        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value
            
        prev_value = value
    
    return total

# Example usage:
print(roman_to_int("XIV"))  # Output: 14'''




# Write a program to find the indices of the most frequently occurring character in a string

'''
def highly_spreaded_char(s):
    l=list(s)
    max_va_index=[]
    max_char=max(l.count(i) for i in l)

    for i in range(len(l)):
        if l.count(l[i]) == max_char:
            max_va_index.append(i)
    return max_va_index


# Example usage:
s= "hello"
highly_spreaded_char(s) 

for i in highly_spreaded_char(s):
    print(i,end=' ')  # Output: 2, 3 (indices of 'l' in "hello")'''





# Write a program to find all elements in a list that are greater than the next element
'''
def  greter_than_next(l):
    res=[]
    for i in range(len(l)):
        if i+1<len(l) and l[i]>l[i+1] :
            res.append(l[i])
    return res


# Example usage:
l = [1, 3, 2, 5, 4]
print(greter_than_next(l))  # Output: [3, 5]'''