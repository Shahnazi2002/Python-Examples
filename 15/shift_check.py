# Given two strings A and B, return whether or not A can be shifted some number of times to get B.
# For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.

def shift_check(a: str, b: str):
    try:
        if b == "":
            return a == b
        else:
            return a == b[(len(b) - a.index(b[0])) :] + b[: (len(b) - a.index(b[0]))]
    except:
        return False


print(shift_check("abcdefg", "cdefgab"))
