class DynamicArray:
    def __init__(self):
        self.capacity = 10
        self._size = 0
        self.fixed_array = [None] * self.capacity

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError('Index out of bounds')
        return self.fixed_array[index]

    def set(self, index, value):
        if index < 0 or index >= self._size:
            raise IndexError('Index out of bounds')
        self.fixed_array[index] = value

    def size(self):
        return self._size

    def append(self, element):
        if self._size == self.capacity:
            self.resize(self.capacity * 2)
        self.fixed_array[self._size] = element
        self._size += 1

    def resize(self, new_capacity):
        new_fixed_size_array = [None] * new_capacity
        for i in range(self._size):
            new_fixed_size_array[i] = self.fixed_array[i]
        self.fixed_array = new_fixed_size_array
        self.capacity = new_capacity

    def pop_back(self):
        if self._size == 0:
            raise IndexError('Pop from empty array')
        self._size -= 1
        if self._size / self.capacity < 0.25 and self.capacity > 10:
            self.resize(self.capacity//2)

    def pop(self, i):
        """
        n is the elements in the array
        Time Complexity: O(n)
        Space Complexity: O(n)
        Worst Case: O(n)
        Amortized time: O(n)
        """
        if i < 0 or i > self._size:
            raise IndexError('Index out of bounds')
        saved_element = self.fixed_array[i]

        # Starting at index, replace elements with their elements to the right.
        for index in range(i, self._size - 1):
            self.fixed_array[index] = self.fixed_array[index + 1]
        self.pop_back()
        return saved_element

    def contains(self, element):
        """
        n is the number of elements in the array
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        for i in range(self._size):
            if self.fixed_array[i] == element:
                return True
        return False

    def insert(self, index, element):
        if self._size == self.capacity:
            self.resize(self.capacity * 2)

    def remove(self, element):
        """
        n is the number of elements in the array
        Time Complexity: O(n)
        Space Complexity: O(n)
        Worst Case: O(n)
        Amortized time: O(n)
        """
        index = 0
        for i in range(self._size):
            if self.fixed_array[i] != element:
                index += 1
                continue
            else:
                index += 1
                self.fixed_array[i] = None
                self._size -= 1
                if self._size / self.capacity < 0.25 and self.capacity > 10:
                    self.resize(self.capacity // 2)
                return index
        return -1
