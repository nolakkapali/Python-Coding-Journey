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

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#list as functional argument
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

#list as return value
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])


def display_car(vehicle):
  print(vehicle)
  return ["mercedez"]
cars=["lambourghini","porche","bmw"]
new_cars=display_car(cars)
print(new_cars)
print(cars)
print(type(new_cars))
print(type(cars))
#return value in function
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

#positional only argument expected by ,/
def my_name(name,age,/):
  print("hello",name,age)
my_name("ella,","Combodia")
#my_name(name="ira","Nepal") #just only accepts positional argument cuz of ,/
#combining positional and keyword argument only
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)

#only keyword argument
def my_name(*,name,city):
  print("Hello",name,city)
my_name(name="aditi",city="Uphill")
#my_name("aditi",city="Uphill") #only keyword argument is passed not positional argument
