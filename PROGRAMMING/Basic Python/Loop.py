#FOR LOOP
'''
Syntax of for Loop
for val in sequence:
	Body of for
'''
#range function

#for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#break statement 
for x in fruits:
  print(x)
  if x == "banana":
    break 

#Looping Through a String
for i in range(5):
 print(i)

for x in "banana":
  print(x)    
print(range(10))

print(list(range(10)))

print(list(range(2, 8)))

print(list(range(2, 20, 3))) 

#range using increment
#The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

for x in range(2, 10, 2):
  print(x)

 #val function
 # Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# iterate 
for val in numbers:	
 print("The sum is", val)

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
	sum = sum+val

print("The sum is", sum)

'''
LOOPING

1.  FOR

2. WHILE

3. BREAK

4. CONTINUE

5. RANGE(). '''

'''
MULTIPLE IF CONDITIONS



#if ,else,else f statement should be followed by a colon.

generally if condition is correct it will produce value or statement entered under if condition , it will not check the else and if else .

to check or print to conditions we have to use 2 if conditions accordingly

eg.



x=2

y=2

z=2





if(x==y):

     print("x is equal to y")

if(x==z):

     print("x is equal to z")

else:



output

x is equal to y

x is equal to z '''

'''
NESTED IF CONDITIONS



nested if is basically used to check more than 2 conditions in one if statement.

if condition which has another if or more if conditions in itself is nested if else.

eg



if (x ==y):

     if(x ==z):

          if(y ==z):

              if(x>y):

                   print("")
else:

    print("")



3:19'''