# function
def add(x, y):
  #print(x+y)
  return (x+y)
print("This is the main function!!!")
c=add(3, y=2)
print("This is the answer!!!",add(3,y=2))
#--------------------------------------------------


def avg_number(x, y):
    e=(x+y)/2
    print("Average of ", x, " and ", y, " is ", (x+y)/2)
    print("You are saying that average of",x,"and",y,'is',e)
avg_number(3, 4)

def nsquare(p,q):
   return p*p+2*p*q+q*q
k=nsquare(2,3)
print("The square of sum p and q is",k)