height=float(input("Enter your height: "))
weight=float(input("Enter your weight: "))
bmi= weight/(height/100)**2
print("Your BMI is ", bmi)

if bmi <= 18.9:
    print("You are underweight")
elif bmi <= 23.5:
    print("Yoi are healthy. Keep it up!")
elif bmi <= 30.2:
    print("You are overweight")
elif bmi <= 37.8:
    print("You are obese")
else:
    print("Exercise more to reduce weigth and become healthy")