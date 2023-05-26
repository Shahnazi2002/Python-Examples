from random import randint
repeat = True
while repeat:
    m = input("Press Enter to roll a die.")
    if m == "":
        n = randint(1, 6)
        if n == 1:
            print("[1]")
        elif n == 2:
            print("[2]")
        elif n == 3:
            print("[3]")
        elif n == 4:
            print("[4]")
        elif n == 5:
            print("[5]")
        elif n == 6:
            print("[6]")
    else:
        repeat = False
        print("End of program.")
