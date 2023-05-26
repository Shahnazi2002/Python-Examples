# This program tells us whether two numbers are multiples or not
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

if first == second:
    print("The entered numbers are equal")
elif first % second == 0:
    print(first, "is a multiple of", second)
elif second % first == 0:
    print(second, "is a multiple of", first)
else:
    print("The entered numbers are not multiples")
