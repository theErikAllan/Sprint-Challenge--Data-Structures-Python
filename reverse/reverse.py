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

    def reverse_list(self, node, prev):
        # First, we check to see if there is a node, and if there isn't, we end the recursion.
        if not node:
            return

        # Second, we check to see if the next node exists, and if it doesn't, we set the current node as the head node. This turns the tail of the old list into the head of the reversed list.
        if node.get_next() == None:
            self.head = node
            return

        # Then we set the next node to a variable in order to use it as the current node when we recursively call the reverse_list() method. We also set the current node as the previous node when we call reverse_list().
        next_node = node.get_next()
        self.reverse_list(next_node, node)
        
        # Once the list has been traversed, we change the pointers by setting the next node of the new head (previously the tail) to the current node and then eliminate the pointer of the current node. We do that for each node until the list is reversed.
        node.get_next().set_next(node)
        node.set_next(None)