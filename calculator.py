def Addition(add1,add2):
    return int(add1)+int(add2)
def Subtraction(sub1, sub2):
    return int(sub1)-int(sub2)
def Multiplication(mul1,mul2):
    return int(mul1)*int(mul2)
def Division(div1,div2):
    return int(div1)/int(div2)
print("***Welcome To Calculator App***\n" \
"*********************Menu************************\n"
"***********Please Choose Any Operation-**********")
while True:
    print("1.Addition\n2.Subtraction\n3.Multiplicatino\n4.Division")
    op=int(input("PLease Select any operation:"))
    a,b=input("Enter two numbers separate them with space:").split()
    if op==1:
        print(Addition(a,b))
    elif op==2:
        print(Subtraction(a,b))
    elif op==3:
        print(Multiplication(a,b))
    else:
        print(Division(a,b))

    pg=input("Exit(Yes/No):")
    if pg=="Yes" or "yes" or"y":
        break





