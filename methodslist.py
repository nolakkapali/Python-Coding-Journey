#append function always adds the element in the last position
a=list((1,2,3,4,5,6))
print(a)
a.append(7)
a.append(8)
a.append(9)
print(a)
b=(1,2,3,4)
print((a.extend(b)))
print(a)
a.insert(2,"ok")
print(a)
fruit=["apple","cherry","rasphberry","rubhab","strawberry"]
fruit[4:]=["banana","cucumber","blackberry","mulberry"]# fruit[4]=["banana","cucumber","blackberry","mulberry"] erokom hole oi 4 number ghor e pura list ta hubhu boshe jabe
print(len(fruit))# kintu [4:] mane hocche 4 number theke ja ache shes prjnto tokhn list er bhetor er item gula boshbe
print(fruit)
fruit[1:4]=["Burberry"]
print(fruit)
#removing--del-delete the entire list,clear()-empty the list,pop()--based on index,remove()
names=["anna","milo","shila","taniya","jackie","chris"]
names.remove("anna")
print(names)
names.pop(0)
print(names)
names.pop()#last member ke pop out korbe
print(names)
del names[0]
print(names)
del names[1:3]
print(names)
names.clear()#it does not take any argument
print(names)
del names
#print(names)
#sorting
num=["A","Balenciaga","ZZ","Channel","Dior","Fendi","Gucci","Hermes","Louie Vutton","Prada","Saint Laurant","Tommy Hilfiger","Valentino","Vivien Westwood"]
num.sort()
print(num)
num.sort(reverse=True)
print(num)
custom_sort=["gh","AS","YSL","Dfcg"]
custom_sort.sort(key=str.upper)
#or
#custom_sort.sort(key=str.lower) ekane iterate korar somoi lower e convert kore compare kore original value list e sort kore boshai
print(custom_sort)
#copying
num2=custom_sort.copy()
print(num2)
num3=list(num2)#using list()constructor
print(num3)
num4=num3[:]#using slicing
print(num4)
#joining of lists
num5=num3+num4
print(num5)
num6=[6467,6546]
for i in num5:
    num6.append(i)
print(num6)
num7=[1,2,3,675,657]
num7.extend(num6)
print(num7)
#indexing
color=["yellow","green","yellow","cirulian blue","white","black","turquoise","cirulian blue"]
print(color.index("cirulian blue",2,6))#it returns the index number and the first occurence
#count
print(color.count("yellow"))#it return the counting value