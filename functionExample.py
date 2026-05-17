# def myfunc():
#   x = 300
# def myinnerfunc():
#     print(x)
# myinnerfunc()

# myfunc() Ans: x name is not defined

# def myfunc():
#   global x
#   x = 300
# def myinnerfunc():
#     print(x)
# myinnerfunc()

# myfunc()

#function e value chara maan shbar prthom boshbe parameter e ar defalut value soho parameter erpor e boshbe
def fruits(weight,name="apple", color="red"):#jaar jonno weight age e boshe ekane
   print("these are",name,"weight=",weight,"color is=",color)
fruits(23,color="yellow")

def my_function(name,age=34):
  print("Hello",name,",","age of",age)

my_function(name = "Emil")