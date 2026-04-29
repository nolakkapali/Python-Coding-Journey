#declare a list way-1
k=list()
print(k)
#declare a list way-2
q=[1,2,3,4,5,6,7,8,9,10]
print(q)
print(type(q))
x=range(5)
print(x)
r=[1,2,3,4,["g","h","j"],"ty","gfh"]
print(r[4][0])
print(r[4][1])
print(r[4][2])
print(r[5])
print(r[6])
dev=("abc")
new=list(dev)
print(new)
print(type(new))
print("a" in new)
name,age,job=new
print(name)
print(age)
print(job)
print(new)
print(new[1:4:2])
num=[1,2,3,4,5]
num.append(9)
print(num)
num1=[23.43,1,21,1,1212,44,3,23]
num1.sort()
print(num1)
print(num+num1)
a=[1,2,3,4]
b=[3,4,5]
a.append(b)# direct list ta eshe boshe jai ekta index e
a.extend(b)# b er itemgula individually a te add hoi
print(a)
print(a)