from random import randint

def rand5():
    return randint(1, 5)

def rand7():
    nums = rand5()+rand5()+rand5()+rand5()+rand5()+rand5()+rand5()
    return (nums%7)+1


print(rand7())