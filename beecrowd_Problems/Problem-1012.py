# Make a program that reads three floating point values: A, B and C. Then, calculate and show:
# a) the area of the rectangled triangle that has base A and height C.
# b) the area of the radius's circle C. (pi = 3.14159)
# c) the area of the trapezium which has A and B by base, and C by height.
# d) the area of ​​the square that has side B.
# e) the area of the rectangle that has sides A and B.

# Input
# The input file contains three double values with one digit after the decimal point.

# Output
# The output file must contain 5 lines of data. Each line corresponds to one of the areas described above, always with a corresponding message (in Portuguese) and one space between the two points and the value. The value calculated must be presented with 3 digits after the decimal point.
A,B,C=input().split()
Abase=float(A)
Base=float(B)
Cheight=float(C)
tri=0.5*Abase*Cheight
cir=3.14159*(Cheight**2)
trap=0.5*(Abase+Base)*Cheight
quad=Base*Base
ret=Abase*Base
print(f"TRIANGULO: {tri:.3f}")
print(f"CIRCULO:{cir:.3f}")
print(f"TRAPEZIO:{trap:.3f}")
print(f"QUADRADO:{quad:.3f}")
print(f"RETANGULO:{ret:.3f}")