# First comment
class RingBuffer:
    def __init__(self, capacity):
        self.size = 0
        self.storage = []
        self.capacity = capacity
        self.oldest = 0

    def append(self, item):
        # The append method adds the given item to the buffer
        if self.size < self.capacity:
            self.storage.append(item)
            # print("This is self.storage: ", self.storage)
            self.size += 1
            # print("This is self.size: ", self.size)
        elif self.size == self.capacity:
            self.storage[self.oldest] = item
            # print("This is self.storage: ", self.storage)
            self.oldest += 1
            # print("This is self.oldest: ", self.oldest)
            if self.oldest == self.capacity:
                self.oldest = 0
        # We need a variable to track the oldest item in the list and increase
        # If the length equals the capacity, subtract the capacity from the variable tracking the oldest item

    def get(self):
        # The get method should return the present state of the ring buffer list
        print(self.storage)
        return self.storage


buffer = RingBuffer(3)
buffer.get()

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f']