# def myfunc():
#   x = 300
# def myinnerfunc():
#     print(x)
# myinnerfunc()

# myfunc() Ans: x name is not defined

def myfunc():
  global x
  x = 300
def myinnerfunc():
    print(x)
myinnerfunc()

myfunc()