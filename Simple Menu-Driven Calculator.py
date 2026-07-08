# ==========================================
# Simple Menu-Driven Calculator
# ==========================================

while True:

    print("\n========== SIMPLE CALCULATOR ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # Exit Program
    if choice == "6":
        print("Thank you for using the calculator.")
        break

    # Invalid Menu Choice
    elif choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid menu choice. Please try again.")

    else:
        count = int(input("How many numbers do you want to enter? "))

        if count <= 0:
            print("Please enter at least one number.")
            continue

        # ---------------- Addition ----------------
        if choice == "1":
            result = 0

            for i in range(count):
                num = float(input(f"Enter number {i + 1}: "))
                result += num

            print("Result =", result)

        # ---------------- Subtraction ----------------
        elif choice == "2":
            result = float(input("Enter number 1: "))

            for i in range(2, count + 1):
                num = float(input(f"Enter number {i}: "))
                result -= num

            print("Result =", result)

        # ---------------- Multiplication ----------------
        elif choice == "3":
            result = 1

            for i in range(count):
                num = float(input(f"Enter number {i + 1}: "))
                result *= num

            print("Result =", result)

        # ---------------- Division ----------------
        elif choice == "4":
            result = float(input("Enter number 1: "))

            valid = True

            for i in range(2, count + 1):
                num = float(input(f"Enter number {i}: "))

                if num == 0:
                    print("Division by zero is not allowed.")
                    valid = False
                    break

                result /= num

            if valid:
                print("Result =", result)

        # ---------------- Modulus ----------------
        elif choice == "5":
            result = float(input("Enter number 1: "))

            valid = True

            for i in range(2, count + 1):
                num = float(input(f"Enter number {i}: "))

                if num == 0:
                    print("Modulus by zero is not allowed.")
                    valid = False
                    break

                result %= num

            if valid:
                print("Result =", result)