""" common product problem """

# def common_product(n,a,b):
#   a1=set(a)
#   b1=set(b)
#   smallest_pair=None
#   for i in a:
#     for j in b:
#       product= i*j

#       if product not in a1 and product not in b1:
#         if smallest_pair is None or (i,j)<smallest_pair:
#           smallest_pair=(i,j)
#   if smallest_pair:
#     return smallest_pair
#   else:
#     return -1


# n=int(input())
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
# result=common_product(n,a,b)
# print(result)







def common_product(n,a,b):
    a1=set(a)
    b1=set(b)
    smallest_pair=None
    for i in a:
        for j in b:
            product=i*j

            if product not in a1 and product not in b1:
                if smallest_pair is None or (i,j)<smallest_pair:
                    smallest_pair=(i,j)
    if smallest_pair:
      return smallest_pair
    else:
      return -1
        

n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

print(common_product(n,a,b))
        