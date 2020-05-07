# Input: qwertty
# Output: t

# Input: qwerty
# Output: None
# Here's some starter code:


def first_recurring_char(s):
    # naive - make list/sort, find repeated based on last index
    # char_list = list(s)
    # char_list.sort()

    # second pass -> use dict to see if a char has been entered already
    # O(n) efficiency

    # you can iterate over a string in Python, don't need to make it a list
    # char_list = list(s)
    char_dict = {}
    for char in s:
        if char in char_dict:
            return char
        else:
            char_dict[char] = char
    return None


print(first_recurring_char('qwertty'))
# t

print(first_recurring_char('qwerty'))
# None
