# does parentheses matching using StackArray
from stack_array import StackArray
def is_matched(expression):
    lefty = '({['
    righty = ')}]'

    S = StackArray()

    for character in expression:
        if character in lefty:
            S.push(character)

        elif character in righty:
            if S.is_empty():
                return False
            if righty.index(character) != lefty.index(S.pop()):
                return False
    return S.is_empty()