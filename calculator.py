Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Simple Calculator for Beginners
... 
... print("Simple Calculator")
... print("1. Add")
... print("2. Subtract")
... print("3. Multiply")
... print("4. Divide")
... 
... choice = input("Enter choice (1/2/3/4): ")
... 
... num1 = float(input("Enter first number: "))
... num2 = float(input("Enter second number: "))
... 
... if choice == '1':
...     print("Result:", num1 + num2)
... 
... elif choice == '2':
...     print("Result:", num1 - num2)
... 
... elif choice == '3':
...     print("Result:", num1 * num2)
... 
... elif choice == '4':
...     if num2 != 0:
...         print("Result:", num1 / num2)
...     else:
...         print("Error! Division by zero is not allowed.")
... 
... else:
...     print("Invalid choice")
