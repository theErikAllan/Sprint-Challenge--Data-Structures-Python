class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False
    def print_helper(self, node, name):
        if node is None:
            print(name + ": None")
        else:
            print(name + ":" + node.value)

    def reverse_list(self, node, prev):
        # first, w
        if not node:
            return prev
        if not node.get_next():
            self.head = node
            
        next = node.get_next()
        node.set_next(prev)
        # self.print_helper(next, "PREV")
        # self.print_helper(node, "HEAD")
        prev = node
        node = next
        return self.reverse_list(node=self.head, prev=None)


        # if self.head is None or self.head.next_node is None:
        #     return self.head
        # else:
        #     self.prev = self.head
        #     self.head = self.head.next_node
        #     self.print_helper(self.prev, "PREV")
        #     self.print_helper(self.head, "HEAD")
        #     self.reverse_list(self.head, self.prev)
        # print(self.head.value)
        

llist = LinkedList()
llist.add_to_head(1)
llist.add_to_head(2)
llist.add_to_head(3)
llist.add_to_head(4)
llist.add_to_head(5)
print(llist)

llist.reverse_list(llist.head, None)