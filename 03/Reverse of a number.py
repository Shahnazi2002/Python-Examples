intinput = int(input("Please enter a number: "))
reverse = 0
while (intinput > 0):
    remainder = intinput % 10
    reverse = (reverse * 10) + remainder
    intinput = intinput // 10
print("The reverse number:", reverse)
