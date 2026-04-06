s="this is jhon doe"
# q= True
# print(f'this is string interpolation value is {q}')
# print (s)
#reverse string using for loop and index
# index=-1
# for i in s:
#     #print(i)
#     print(s[index])
#     index=index-1

#reverse string using while loop
t=input("Enter String:")
pattern=input("enter indexing pattern (straight/reverse):")
if pattern == "straight":
    index=0
else:
    index=-1
print(len(t))
while len(t)>index:
        if len(t)==index+1:
            break
        print(t[index])
        index = index-1
        elif index == -len(t):
            break
    else:
        index==-1
        if len(t) == index+1:
            break
        index = index-1
        elif index == -len(t):
            break