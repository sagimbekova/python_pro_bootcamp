
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi_result = int(weight) / float(height) ** 2
print(round(bmi_result))