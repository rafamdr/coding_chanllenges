from functools import reduce
# ----------------------------------------------------------------------------------------------------------------------


def num_chars(textinput: str, ch: str):
    return reduce(lambda count, c: count + (c == ch), textinput, 0)
# ----------------------------------------------------------------------------------------------------------------------


print(num_chars('hello world!!', 'l'))
print(num_chars('hello world!!', 'h'))
print(num_chars('', 'l'))
print(num_chars('', ''))
print(num_chars('asdasda', ''))
print(num_chars('asdasda', 'asdas'))
# ----------------------------------------------------------------------------------------------------------------------
