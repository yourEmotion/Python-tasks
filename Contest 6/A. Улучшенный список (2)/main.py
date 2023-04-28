class ExtendedList(list):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def reversed(self):
        return self[::-1]

    @property
    def first(self):
        return self[0]

    @first.setter
    def first(self, value):
        self.insert(0, value)

    @property
    def last(self):
        return self[-1]

    @last.setter
    def last(self, value):
        self.append(value)

    @property
    def size(self):
        return len(self)

    @size.setter
    def size(self, new_size):
        if new_size > len(self):
            self.extend([None] * (new_size - len(self)))
        elif new_size < len(self):
            for index in range(new_size, len(self), 1):
                self.pop()

    R = reversed
    F = first
    L = last
    S = size


a = ExtendedList([3, 6, 2, 8])
a.size = 2
print(a.size)
