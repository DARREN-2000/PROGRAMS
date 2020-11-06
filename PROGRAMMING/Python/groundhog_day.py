import time

perfect_number = 12_395

clock1= """
+---+---+---+
| 0 | 0 | 5 |
+---+---+---+"""

clock2= """
+---+---+---+
| 0 | 0 | 4 |
+---+---+---+"""

clock3= """
+---+---+---+
| 0 | 0 | 3 |
+---+---+---+"""

clock4= """
+---+---+---+
| 0 | 0 | 2 |
+---+---+---+"""

clock5= """
+---+---+---+
| 0 | 0 | 1 |
+---+---+---+"""

clock6 = """
+---+---+-------------------+
| * | @ | 0 | O | 0 | @ | * |
+---+---+-------------------+
"""

print("""
+---------------------------------+
|Welcome to Groundhog Day - 2 Feb.|
|You're stuck in 2 February 2020. |
|Enter the perfect number to end  |    
|the loop or be stuck forever...  |
+---------------------------------+
""")

number = int(input("Enter number: "))

while number != perfect_number:
    if number < perfect_number:
        print(clock1)
        time.sleep(1)
        print(clock2)
        time.sleep(1)
        print(clock3)
        time.sleep(1)
        print(clock4)
        time.sleep(1)
        print(clock5)
        time.sleep(3)
        print(clock6)
        time.sleep(2)
        print("February 2\nNumber too low.\n")
        print(" You are still stuck in the same Day!")
    else:
        print(clock1)
        time.sleep(1)
        print(clock2)
        time.sleep(1)
        print(clock3)
        time.sleep(1)
        print(clock4)
        time.sleep(1)
        print(clock5)
        time.sleep(3)
        print(clock6)
        time.sleep(2)
        print("February 2\nNumber too high.\n")
        print(" You are still stuck in the same Day!")

    number = int(input("Enter number: "))

print(clock1)
time.sleep(1)
print(clock2)
time.sleep(1)
print(clock3)
time.sleep(1)
print(clock4)
time.sleep(1)
print(clock5)
time.sleep(3)
print(clock6)
time.sleep(2)        
print("February 3\n Today is tomorrow!\n")
print(" ATALST! Finally u r free from the same day")
