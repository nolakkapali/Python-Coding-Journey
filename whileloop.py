# # while True:
# #     line= input("<")
# #     if line =="done" or line == "Done":
# #      break
# #     print(line)
# # print("Done!")

# n=0
# s=0
# # while (n<10):
# #     print(n)
# #     s = s+n
# #     n=n+1
# #     if (n == 5):
# #         break
# # else:
# #     print("The first 9 inyegers:")
# # print("it breaked",n)
    
# # print("sum:",s)

# n=0
# while(n<10):
#     line=input("Take the word:")
#     if line == "done" or  line == "Done":
#      break
#     n+=1
# else:
#    print("The loop is succesfully finished!!")
# print("Loop not succesfully run!!")
#Smallest number
smallest=None
for i in [1,2,3,4,5,89,0]:
    if smallest is None or i<smallest:
        smallest=i
    else:
        print(f'Smallest so far :{smallest}, I value so far: {i}')
print("Smallest number: ",smallest)    

