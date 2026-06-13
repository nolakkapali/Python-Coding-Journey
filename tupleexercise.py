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
#deleting tuples
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
#remove tuple
dt=("apple","orange","hvj")
ky=list(dt)
ky.remove("hvj")
print(ky)
dt=tuple(ky)
print(dt)
del dt #deletes the tuple entirely