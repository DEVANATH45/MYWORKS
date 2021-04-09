import cmath

def Quadratic_function():
 def input_1():
    print("Enter the elements a,b,c of the quadratic equation:\n")
    a=int(input())
    b=int(input())
    c=int(input())
    r=[a,b,c]
    return r
 def quad(x,y,z):
    s=(y*y)-(4*x*z)
    q=cmath.sqrt(s)
    r1=(-y+q)/(2*x)
    r2=(-y-q)/(2*x)
    return[r1,r2,s]


 r=input_1()
 x=r[0]
 y=r[1]
 z=r[2]

 p=quad(x,y,z)

 print("The equation is :{0}x^2+{1}x+{2}".format(x,y,z))

 if p[2]==0:
    print("Roots are equal\n.")
 elif p[2]<0:
    print("Roots are complex.\n")
 else:
    print("Roots are natural.\n")

 print("Solution to the given equation is:{0},{1}".format(p[0],p[1]))


def ams():
 n=int(input("Enter the number tp check:"))
 temp=n
 times=0
 sum=0
 while temp>0:
    times=times+1
    temp//=10
 temp=n
 while temp>0:
    r=temp%10
    sum=sum+(r**times)
    temp//=10
 if sum==n:
    print("The number is an amstrong number")
 else:
    print("The number is not an amstrong number")


def factorial():
    def fact(n):
        fac = 1
        for i in range(1, n + 1):
            fac = fac * i
        return fac

    n = int(input("Enter the number:"))
    if n < 0:
        print("Enter a postive number!!")

    elif n == 0:
        print("Factorial of the given number is:0")
    else:
        print("Factorial of the given number is :" + str(fact(n)))

def error():
    print("Invalid input.")


def simple():
 def getno():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    return a,b

 def add():
    x,y=getno()
    return x+y

 def sub():
    x,y=getno()
    return x-y

 def mul():
    x,y=getno()
    return x*y

 def div():
    x,y=getno()
    return x/y

 def error():
    print("Invalid input")


 print("* * * * * * * * * * * *\n"
       "*   1.Addtion         *\n"
       "*   2.Subtraction     *\n"
       "*   3.Multiplication  *\n"
       "*   4.Divison         *\n"
       "* * * * * * * * * * * *\n")
 ch = int(input("Enter the choice(1-4):"))

 op ={
    1:add,
    2:sub,
    3:mul,
    4:div,
     }
 output=op.get(ch,error)()
 print("Answer is :"+str(output))




choice='Y'
while choice=='y' or choice=='Y':
 print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n"
       "*                                                       *\n"
       "*                                                       *\n"
       "*              1.Quadratic Equation                     *\n"
       "*              2.Amstrong Number check                  *\n"
       "*              3.Factorial                              *\n"
       "*              4.Simple Calculator                      *\n"
       "*                                                       *\n"
       "* * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
 op={
    1:Quadratic_function,
    2:ams,
    3:factorial,
    4:simple
  }
 ch=int(input("Enter the choice(1-4):"))
 op.get(ch,error)()
 choice=input("Do you want to enter again[Y/N]?")
























