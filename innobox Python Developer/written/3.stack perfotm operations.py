def perform_operations(n,s,temp):
    result=list(s)
    for operation in temp:
        if operation =='add':
            result.append('x')
        elif operation=='delete':
            result.pop()
    return ''.join(result)[::-1]


n=int(input())
s=input().strip()
temp=(input().split())

print(perform_operations(n,s,temp))