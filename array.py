"""
Data Structure: Array
Dynamic Arrray
"""

class DynamicArray:
    """This class creates  a dynamic array with limited functionality"""

    def __init__(self):
        """create empty array"""
        self._n = 0  # number of elements in the array
        self._capacity = 1  # capacity of the array
        self._A = self._make_array(self._capacity)

    def __len__(self):
        """returns length of array"""
        return self._n

    def size(self):
        """returns size of array"""
        return self._n

    def capacity(self):
        """returns the capacity of the array"""
        return self._capacity

    def is_empty(self):
        """return true if the array is empty else false"""
        if self._n == 0:
            return True
        return False

    def at(self, k):
        """returns element at position k"""
        if self._A[k]:
            return self._A[k]
        raise IndexError('index out of bound')

    def push(self, value):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = value
        self._n += 1

    def __getitem__(self, k):
        """returns the item at given position"""
        if not 0 <= k < self._n:
            raise IndexError('Index Error')
        return self._A[k]

    def append(self, obj):
        """appends a new element to the list"""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def prepend(self, value):
        """insert new value at position 0"""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, 0, -1):
            self._A[j] = self._A[j - 1]
        self._A[0] = value
        self._n += 1

    def insert(self, k, value):
        """ insert a value at position k """
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, - 1):
            self._A[j] = self._A[j - 1]
        self._A[k] = value
        self._n += 1

    def pop(self):
        self._A[self._n - 1] = None
        self._n -= 1

    def delete(self, index):
        for k in range(index + 1, self._n - 1):
            self._A[k - 1] = self._A[k]
        self._n -= 1

    def find(self, value):
        for k in range(self._n):
            if self._A[k] == value:
                return k
        raise ValueError('value does not exist')

    def remove(self, value):
        """removes item from array"""
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k + 1, self._n):
                    self._A[j - 1] = self._A[j]
                self._n -= 1
                return
        raise ValueError('value not found')

    def _resize(self, c):
        """resizes the array"""
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        """doubles the size of the array"""
        return c * [None]

lst = DynamicArray()
print(lst)
lst.append(1)
print(lst[0])
lst.append(2)
print(lst[1])
print(lst.__len__())
lst.insert(0, 0)
print(lst[0])
print(lst[1])
print(lst[2])
lst.remove(0)
print(lst[0])
print(lst[1])

