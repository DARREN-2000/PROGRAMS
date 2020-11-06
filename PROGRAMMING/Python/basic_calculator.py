while True:
    print("""
Calculator:
+---------+

+---------+
| [+] [-] |
| [*] [/] |
+---------+
    """)

    number1 = float(input("First number: "))
    operator = input("Operator: ")
    number2 = float(input("Second number: "))

    if operator == "+":
        total = number1 + number2
    elif operator == "-":
        total = number1 - number2
    elif operator == "*":
        total = number1 * number2
    elif operator == "/":
        total = number1 / number2
    else:
        total = "Invalid operator"

    print("\nAnswer:")
    print("+---------+")
    print(total)
    print("+---------+")

    again = input("Calculate again?: ")
    valid_answers = ("Yes", "yes", "Y", "y")
    if again not in valid_answers:
        break
    
