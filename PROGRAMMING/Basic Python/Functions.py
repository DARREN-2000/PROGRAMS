
FUNCTIONS

def add(x,y):                   # : "colon" is compulsory while defining a function

       z = x+y                     # after first line,indendation is compulsory

       return print(z)          # after defining a function,  we have to return the function

a = 1

b = 2

add(a,b)



c = 2

d= 3

add(a,b)



output

3

5



note : in function the inside the parameter, the values given are just an example to create an method or formula which we are going to execute with user defined or user entered values  or default values assigned by user after returning an function.



PARAMETERS



1. actual parameters

2. default parameters



* default parameters

def add(x,y=1):

      z= x+y

     return print(z)

a=int(input("enter value"))

add(a)



output

enter value 3

4


FUNCTION MODIFICATION

eg. zero division error



def add(a,b):

       if(b == 0)

           print(" fuck off")

      else:

           c = a/b

           return print(c)

a=int(input("a="))

b=int("input(b="))

add(a,b)



output

a=4

b=2

2.0



a=4

b=0

fuck off



note: we can modify the function by condition,formulas etc........


METHODS

some of the inbuilt functions which performs specific actions on specific data types is called as   method()

eg.

len("name")

2



to view all methods

dir("data type")

dir("list")

dir("tuple")

dir("dictionary")

dir("string")