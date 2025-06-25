class DynamicArray:
    def __init__(self, elements):
        self.array = [elements]

    def append(self, element):
        """adds element x to the end of the array"""
        pass

    def get(self, index):
        """returns the element at index"""
        for position, element in enumerate(self.array):
            if position == index:
                return element

    def set(self, index, value):
        """updates the preexisting element at index to be value"""
        for position, element in enumerate(self.array):
            if position == index:
                self.array[index] = value

    def size(self):
        """returns the number of elements in the array"""
        count = 0
        for element in self.array:
            count += 1
        return count

    def pop_back(self):
        """Removes the last element"""
        last_position = self.size()
        del self.array[last_position]

    def pop(self, index):
        """
        n is the elements in the array
        Time Complexity: O(n)
        Space Complexity: O(n)
        Worst Case: O(n)
        Amortized time: O(n)
        """
        if index < 0 or index > self._size:
            raise IndexError('Index out of bounds')
        popped = self.fixed_array[index]

        for i in range(self._size):
            if i < index or i == index:
                continue
            else:
                self.fixed_array[i - 1] = self.fixed_array[i]
        self._size -= 1

        if self._size / self.capacity < 0.25 and self.capacity > 10:
            self.resize(self.capacity//2)

        return popped
