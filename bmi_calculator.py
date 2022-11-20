
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi_result = round(weight / height ** 2)

if bmi_result <= 18.5:
    print(f"Your BMI is {bmi_result}, you are underweight.")
elif bmi_result > 18.5 and bmi_result <= 25:
    print(f"Your BMI is {bmi_result}, you have a normal weight.")
elif bmi_result > 25 and bmi_result <= 30:
    print(f"Your BMI is {bmi_result}, you are slightly overweight.")
elif bmi_result > 30 and bmi_result <= 35:
    print(f"Your BMI is {bmi_result}, you are obese.")
elif bmi_result > 35:
    print(f"Your BMI is {bmi_result}, you are clinically obese.")