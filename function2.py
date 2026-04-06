def nsquare(x, y=3):
    return (x*x + 2*x*y + y*y)


print("The square of the sum of 2 and 2 is : ", nsquare(2))
print("The square of the sum of 2 and 3 is : ", nsquare(2, 4))

def greet(name):
   print(f"how are you, {name}?")
   return f"Hello, {name}"
c=greet("Mina Rani")
print(c)