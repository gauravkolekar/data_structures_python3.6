# empty list which is gonna act like stack
stack_list = list()

def is_matching(expression):
    opening = '({['
    closing = ')}]'

    for charcter in expression:
        if charcter in opening:
            stack_list.append(charcter)
        else:
            if len(stack_list) == 0:
                return False
            if closing.index(charcter) != opening.index(stack_list.pop()):
                return False
    return True
print(is_matching('()(()){([()])}'))
print(is_matching(')(()){([()])}'))
