presentdays = int(input("Working days: "))
absentdays = int(input("Non-working days/ sick leaves: "))
attendeddays = presentdays-absentdays
print("The total number of attended wprking days are ", attacheddays)

eligibility = ("attacheddays/presentdays")
print("You will only be eligible to write the exam, your attendance must be 75% and above: ", eligibility)

if eligibility <=75:
    print("You are not eligible to write the examination")
else: 
    print("You are eligble to write the examination")