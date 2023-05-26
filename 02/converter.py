print("Convert Fahrenheit to Celsius and vice versa")
print("Please choose the primary unit")
primary = input("enter (F) for Fahrenheit and (C) for Celsius: ")

try:
    if primary.lower() == "f":
        f = float(input("Enter the temperature in Fahrenheit: "))
        c = (f - 32) / 1.8
        print("The temperature in Celsius is", round(c, 1))
    elif primary.lower() == "c":
        c = float(input("Enter the temperature in Celsius: "))
        f = (c * 1.8) + 32
        print("The temperature in Fahrenheit is", round(f, 1))
    else:
        print("The value entered is not supported.")
except:
    print("Something went wrong!")
    print("Please restart the program and enter the correct values.")
