class Empty(Exception):
    pass


class StackArray:
    """this is a implementation of stacks using array"""
    def __init__(self):
        self._data = list()

    def __len__(self):
        """return length of stack"""
        return len(self._data)

    def is_empty(self):
        """return if stack is empty"""
        return len(self._data) == 0

    def push(self, e):
        """add element to top of stack"""
        self._data.append(e)

    def top(self):
        """returns element at top of stack"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        """removes element top of the stack"""
        if self.is_empty():
            raise Empty('stack is empty')
        return self._data.pop()

S = StackArray()
print(S)
S.push(5)
S.push(3)
print(S._data)
print(len(S))
