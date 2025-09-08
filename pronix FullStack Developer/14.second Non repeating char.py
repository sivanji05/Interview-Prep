
# def second_non(s):
#     char_count={}
#     for i in s:
#         if i in char_count:
#             char_count[i]+=1
#         else:
#             char_count[i]=1
#     non_repating_cahr = [char for char in s if char_count[char]==1]

#     if len(non_repating_cahr)<2:
#         return None
#     return non_repating_cahr[1]


# s="sivanji"
# print(second_non(s)) #v



s="sivanji"
l={}
for i in s:
    if i in l:
        l[i]+=1
    else:
        l[i]=1
# l1=[]
# for k,v in l.items():
#     if v==1:
#         l1.append(k)
non_re=[c for c in s if l[c]==1]
print(non_re)
print(non_re[1])




