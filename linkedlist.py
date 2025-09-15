class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return self.data
    
class LinkedList:
    def __init__(self, nodes = None):
        self.head = None
        if nodes is not None:
            node = Node(data = nodes.pop(0))
            self.head = node
            for elemn in nodes:
                node.next = Node(data = elemn)
                node = node.next

    def __repr__(self):
        if self.head is not None:
            node = self.head
            cur = []
            while node is not None:
                cur.append(node.data)
                node = node.next
            cur.append("None")
            return " -> ".join(cur)
        else:
            return "None"

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node
    
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node
    
    def add_after(self, target_node, value_node):
        if self.head is None:
            raise Exception("List is empty")
            
        for node in self:
            if node.data == target_node:
                value_node.next = node.next
                node.next = value_node
                return

        raise Exception("Node with data '%s' not found" % target_node)
    
    def add_before(self, target_node, value_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node:
            self.add_first(value_node)
            return 
        
        prev_node = self.head
        for node in self:
            if node.data == target_node:
                prev_node.next = value_node
                value_node.next = node
                return
            prev_node = node
        
        raise Exception("Node with data '%s' not found" % target_node)

    def remove_node(self, value_node):
        if self.head is None:
            raise Exception("List is empty")
        
        if self.head.data == value_node:
            self.head = self.head.next
            return
        

        prev_node = self.head
        for node in self:
            if node.data == value_node:
                prev_node.next = node.next
                return 

            prev_node = node

        raise Exception("node with data '%s' not found" % value_node)
    
    def remove_first(self):
        if self.head is None:
            raise Exception("List is empty")


        val = self.head.data
        self.head = self.head.next
        return val




    def get_position(self, index):
        if index < 0:
            raise Exception("Index not valid")
        if self.head is None:
            raise Exception("List is empty")
        
        i = 0
        for node in self:
            if i == index:
                return node
            i+= 1
        raise IndexError("Index out of range")

    def reversed(self):
        cur = LinkedList()
        for node in self:
            new_node = Node(node.data)
            cur.add_first(new_node)

        return cur


class Queue(LinkedList):
    def __init__(self, nodes=None):
        super().__init__(nodes)

    def enqueue(self, value):
        self.add_last(Node(value))

    def dequeue(self):
        return self.remove_first()
        

llist = LinkedList(["a", "b", "c", "d"])
print(llist)

for node in llist:
    print(node)

print(llist.reversed())