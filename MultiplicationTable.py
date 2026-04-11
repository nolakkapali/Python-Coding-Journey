for i in [1,2,3,4,5,6,7,8,9,10]:
    for j in [1,2,3,4,5,6,7,8,9,10]:
        print(f'{i} X {j} = {i*j}')
    print("\n")

#Left Aligned Triangle
# n=int(input("Users enter:"))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#        print("*",end=" ")
#        j=j+1
#     print("\n")
#     i+=1

#Right Aligned Triangle
k=int(input("Users enter:"))
i=1
while i<=k:
    j=5
    while j>k-i:
       print("*",end=" ")
       j=j-1
    print("\n")
    i+=1
