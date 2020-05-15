# First comment
class RingBuffer:
    def __init__(self, capacity):
        self.size = 0
        self.storage = []
        self.capacity = capacity
        self.oldest = 0

    def append(self, item):
        # The append method adds the given item to the buffer

        # First, we check to see if the size of the buffer is less than the capacity
        if self.size < self.capacity:
            # if the size of the buffer is less than the total capacity, we just append the desired item to the buffer and increase the size counter by 1
            self.storage.append(item)
            self.size += 1
        # Once the size of the buffer reaches the capacity, we want to overwrite the element in the oldest index
        elif self.size == self.capacity:
            # So we overwrite the element in the oldest index and increase self.oldest by 1 so the oldest is now 1 place to the right
            self.storage[self.oldest] = item
            self.oldest += 1
            
            # finally, once self.oldest reaches the capacity, the oldest element is now in index 0 again, so we must reset the tracker
            if self.oldest == self.capacity:
                self.oldest = 0

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