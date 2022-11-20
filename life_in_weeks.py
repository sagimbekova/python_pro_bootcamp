age = input("What is your current age? ")

year = 90 - int(age)
month = year * 12
week = year * 52
day = year * 365

print(f"You have {day} days, {week} weeks, and {month} months left.")