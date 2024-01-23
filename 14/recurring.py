# Given a string, return the first recurring character in it, or null if there is no recurring character.

def is_recurring(string_in: str):
    recurring_list = []
    for ch in string_in:
        if ch in recurring_list:
            return ch
        else:
            recurring_list.append(ch)


print(is_recurring("ubuntu"))
