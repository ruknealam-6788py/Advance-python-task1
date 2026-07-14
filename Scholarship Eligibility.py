#          scholarship Eligibility 
marks = float(input("Enter your marks under(0-100)"))
attendence = float(input("Enter your attendence percentage under(0-100) "))
if marks < 0 or marks > 100 or attendence < 0 or attendence > 100:
    print("Invalid input")
elif attendence < 75 :
    print("Not eligible for scholarship")
else :
 if marks >= 90 and marks <=100 :
    print("Full scholarship")
 elif marks >= 80 and marks <=89 :
    print("Half scholarship")
 elif marks >= 70 and marks <=79 :
    print("Quarter scholarship")
 elif marks < 70 :
    print("No Scholarship")


    





