print("Welcome in my calculator program 🧮")
print("1️⃣ At first, you have to provide one number. \n2️⃣ Next, please provide an operator. \n3️⃣ At the end provide a second number.")
print("Let's do it 📝")
def calc():
    a = int(input("Enter first number: "))
    operator = input("Enter a math operator: ")
    b = int(input("Enter second number: "))

    while operator in ('+', '-', '*', '**', '/', '%'):
        if operator == '+':
            print(f"Sum of {a} and {b} equals {a+b}")
            break
        elif operator == '-':
            print(f"Diff of {a} and {b} equals {a-b}")
            break
        elif operator == '*':
            print(f"Product of {a} and {b} equals {a*b}")
            break
        elif operator == '/':
            print(f"Quotient of {a} and {b} equals {a-b}")
            break
        elif operator == '**':
            print(f"Number {a} to the power {b} equals {a**b}")
            break
        elif operator == '%':
            print(f"{a} modulo {b} equals {a%b}")
            break
        else:
            print("Operator must be like these on the begin, try again 🚀")
            continue
    decision = input("Do you want to do some more operations 🤔 (type YES or NO) ")
    if decision == 'YES':
        calc()
    elif decision == 'NO':
        print("Thanks you for using my program 🥰")
        print("Goodbye user 👋")
def main():
    calc()
if __name__ == '__main__':
    main()


