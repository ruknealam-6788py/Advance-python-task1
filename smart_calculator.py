print("==== Smart Calculator ====")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Even or Odd")
choice = int(input("Enter your choice (1-5):"))
match choice:
    case 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number:"))
        print("Result = ", num1 + num2)
    case 2:
        num1 = float(input("Enter first number :")) 
        num2 = float(input("Enter second number:"))
        print("Result = ", num1 - num2)
    case 3:
        num1 = float(input("Enter first number :"))
        num2 = float(input("Enter second number :"))
        print("Result = ", num1 * num2)
    case 4:
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))
        if num2 == 0:
            print("Division by zero is not allowed.")
        else:
            print("Result = ", num1 / num2)
    case 5:
            num = int(input("Enter a number :"))
            if num % 2 == 0:
                print(num, "is Even.")
            else:
                print(num,("is odd"))
    case _:
                print ("Invalid menu option.")

       






    

