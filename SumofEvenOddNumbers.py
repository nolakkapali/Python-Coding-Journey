n=int(input("Put range:"))
even_sum=0
odd_sum=0
for i in range(0,n):
    if i%2==0:
        even_sum=even_sum+i
    else:
        odd_sum=odd_sum+i
print("Even Sum:",even_sum)
print("Odd Sume:",odd_sum)