new_string="JohnDoed"
x= len(new_string)+1/2
y=int(len(new_string)/2)
z=int(len(new_string)/2+1)

if (len(new_string)%2!=0):
   print(new_string[0]+new_string[x]+new_string[len(new_string)-1])
else:
   print(new_string[0]+new_string[y-1]+new_string[z-1]+new_string[len(new_string)-1])

# 2Exercise 1B: Create a string made of the middle three characters

def ThreeChar(line):
   l=len(line)
   print(l)
   mid=int(l/2)
   result = line[mid-1:mid+2]
   return result


print(ThreeChar("JhonDipPeta"))
print(ThreeChar("JaSonAy"))

#Exercise 2: Append new string in the middle of a given string

s1 = "Ault"
s2 = "Kelly"
l=len(s1)
mid=int(l/2)
print(s1[0:mid]+s2+s1[mid+1:l])

#Exercise 3: Create a new string made of the first, middle, and last characters of each input string
def stringMerger(s1,s2):
   l=len(s1)/2
   k=len(s2)/2
   mid=int(l)
   mid2=int(k)
   return s1[0]+s2[0]+s1[mid]+s2[mid2]+s1[-1]+s2[-1]
s=stringMerger("America","Japan")
print(s)

#Exercise 4: Arrange string characters such that lowercase letters should come first
s1="PyNaTive"
sum=""
sum1=""
for i in s1:
   if i.islower():
      sum=sum+i
   else:
      sum1=sum1+i
print(sum+sum1)

#Exercise 5: Count all letters, digits, and special symbols from a given string
str1 = "P@#yn26at^&i5ve"
count=0
k=0
g=0
for i in str1:
   if i.isdigit():
       count=count+1
   elif i.isalpha():
      k=k+1
   else:
      g=g+1
print(f"Char={k}\nDigit={count}\nSymbol={g}")

#Find USA count in the given sentence
a = "Welcome to USA. usa awesome, isn't it?"
b=a.upper()
print("The USA Count is:",b.count("USA"))

#numbers to check negative,positive and zero
num=int(input("Enter the number here:"))
if(num>0):
   print("Number is positive")
elif num<0:
   print("Number is negative")
else:
   print("Number is zero")