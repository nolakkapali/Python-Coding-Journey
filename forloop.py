#1.
# sum=0
# for i in range(1,50,2):
#         sum=sum+i
# print("Sum",sum)

#2.
# s=int(input("Enter the number:"))
# for i in range(0,11):
#         print(f"{s} X {i} = {s*i}")  

#3.
# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if (i%5==0 and i>150):
#         print(i)
#     else:
#         print("Not printable!")
    
#4.
# sum=0
# count=0
# while True:
#     s=input("Take the numebers:")
#     if s=="done" or s=="Done":
#         break
#     else:
#         f=float(s)
#         sum = f+sum
#         count = count+1
# print("Average Number:",sum/count)

#5.
# s=int(input("Enter the number:"))
# while s>0:
#     print(s)
#     s=s-1
# print("Blastoff!")    

#6.
# secret_num=4
# while True:
#     s=int(input("the number:"))
#     if s== secret_num:
#         break
# print(f"You gueesed it Right! The secret number is {secret_num}")  

#7.
s=int(input("Enter the number:"))
while s>0:
    if s%2==0:
        print(s)
        break
    s=s+1
else:
    print("The Prime numbers are:")


