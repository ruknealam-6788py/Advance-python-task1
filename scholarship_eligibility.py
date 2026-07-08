marks = float(input("Enter your marks (0-100): "))
attendance = float(input("Enter your attendence percentage(1-100): "))
if marks < 0 or marks > 100 or attendance < 0 or attendance > 100:
    print("Invalid input.")
elif attendance < 75:
    print("Not eligible for scholarship. ")
else:
    if marks >= 90:
        print("Full Scholarship")
    elif marks >= 80:
        print("Half Scholarship ")
    elif marks >= 70:
        print("Quarter Scholarship")
    else:
        print("No Scholarship")

    

