def calculator():
    print("=" * 35)
    print("       SIMPLE CALCULATOR")
    print("=" * 35)
    print("Operations: +  -  *  /  %  ** (power)")
    print("Type 'exit' to quit")
    print("-" * 35)

    while True:
        try:
            num1 = input("\nEnter first number: ")
            if num1.lower() == 'exit':
                print("Goodbye!")
                break

            operator = input("Enter operator (+, -, *, /, %, **): ")
            if operator.lower() == 'exit':
                print("Goodbye!")
                break

            num2 = input("Enter second number: ")
            if num2.lower() == 'exit':
                print("Goodbye!")
                break

            num1 = float(num1)
            num2 = float(num2)

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                    continue
                result = num1 / num2
            elif operator == '%':
                if num2 == 0:
                    print("Error: Cannot modulo by zero!")
                    continue
                result = num1 % num2
            elif operator == '**':
                result = num1 ** num2
            else:
                print("Error: Invalid operator! Use +, -, *, /, %, **")
                continue

            # Clean output: show int if no decimal needed
            if result == int(result):
                print(f"Result: {num1} {operator} {num2} = {int(result)}")
            else:
                print(f"Result: {num1} {operator} {num2} = {result:.4f}")

        except ValueError:
            print("Error: Please enter valid numbers!")

if __name__ == "__main__":
    calculator()
