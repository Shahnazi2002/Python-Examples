n = int(input("Please enter your weight: "))
m = float(input("Please enter your height: "))
bmi = int(100*n/(m*m))
q, r = divmod(bmi, 100)
print(f"{q}.{r}")
if bmi<1850:
    print("Underweight")
elif 1850<=bmi<2500:
    print("Normal")
elif 2500<=bmi<3000:
    print("Overweight")
else:
    print("Obese")