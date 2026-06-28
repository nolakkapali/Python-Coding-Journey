thistuple = ("apple", "banana", "cherry")
print(thistuple)
createtuple=tuple((1,2,3,4,"a","bhjbkd",6))
print(type(createtuple))
print(len(createtuple))
print(createtuple)
#accessing tuple
print(createtuple[2])
print(createtuple[4:7])
print(createtuple[-5:-2])
print(createtuple[-3:-1])
#updating tuples
a=tuple(("a","b","c","d"))
print(a)
b=list(a)
print(type(b))
b[0]=1
print(b)
c=tuple(b)
print(a)
print(c)
#adding tuples
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(y)
y.remove("orange")
thistuple=tuple(y)
print(thistuple)
y[1]="chia seeds"
print(y)
thistuple=tuple(y)
print(thistuple)
x=("kiwi",)#shudu 1 ta item thkle comma dewa lage shes e but 1 er beshi item thkle lage na
thistuple=thistuple+x
print(thistuple)
#deleting tuples
#remove tuple
dt=("apple","orange","hvj")
ky=list(dt)
ky.remove("hvj")
print(ky)
dt=tuple(ky)
print(dt)
del dt #deletes the tuple entirely
#adding tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#packing a tuple means normally assigning value to it
num=(1,2,3,4,5,6)
print("num:",num)
#unpacking a tuple means when values are extracted back into a variable
(one,two,three,four,five,six)=num
print(one)
print(two)
print(three)
print(four)
print(five)
print(six)
print(num)
#using asterisk *- ekane ei * ta jei variable er pashe thake oi
#variable ta ekta list e baki value gula niye nei

flower=("rose","jinilia","jasmine","lily","night queen","tulip","lotus")
(a,b,c,*d,e,f)=flower
print(d)
print(e)
print(f)
thistuple=thistuple+flower
print(thistuple)
thistuple=thistuple * 3
print(thistuple)
print(len(thistuple))

#tuple loop
for i in thistuple:
    print(i)

i=0
while i<len(thistuple):
    print(thistuple[i])
    i=i+1

for i in range(len(thistuple)):
    print("333333333")
    print(thistuple[i])

m=(1,(2,3,4,5),45,(23,45,44,3),56,(556))
i=0
while i < len(m):
    print(i)
    i=2*i+1