#  Temperature
temp = input("Temperature: ")
unit = input("C or F: ")
if unit == "c":
    print("result: " + str(float(temp)*(9/5)+32))
elif unit == "f":
    print("result: " + str((float(temp)+(-32))*(5/9)))
else:
    print("Invalid Entry!")