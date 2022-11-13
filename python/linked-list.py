#!/usr/bin/env python3

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        string = "[ "
        current = self.head
        while current:
            if current != self.head:
                string += " -> "
            string += str(current.data)
            current = current.next
        string += " ]"
        return string

    def prepend(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert(self, data):
        node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            else:
                current = current.next
        return None

    def delete(self, data):
        previous = None
        current = self.head
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                # unlink the node from the list
                current.next = None
                return
            else:
                previous = current
                current = current.next

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def new_reversed_list(self):
        ll = LinkedList()
        node = self.head
        while node != None:
            ll.prepend(node.data)
            node = node.next
        return ll
    
    def append_list(self, llist):
        current = llist.head
        while current:
            self.insert(current.data)
            current = current.next


ll = LinkedList()
ll.insert('l')
ll.insert('e')
ll.insert('g')
ll.insert('o')
print(ll)
ll.delete('e')
ll.prepend('a')
print(ll)

ll2 = ll.new_reversed_list()
print(ll2)

ll3 = LinkedList()
ll3.insert('l')
ll3.insert('e')
ll3.insert('g')
ll3.insert('o')
ll.append_list(ll3)
print(ll)
