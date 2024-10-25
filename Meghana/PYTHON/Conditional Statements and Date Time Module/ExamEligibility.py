presentdays = int(input("Enter the total number of working days: "))
absentdays = int(input("Enter the total number of absent days: "))

attended_days = presentdays - absentdays
print("The total amount of days you have attended are ", attended_days)

eligibility = (attended_days / presentdays) * 100
print("You will only be eligible to write the exam if you presence is more than 75%, you percentage is: ", eligibility)

if eligibility <= 75:
    print("You are not eligible to write the exam")
else:
    print("You are eligible to write the exam")