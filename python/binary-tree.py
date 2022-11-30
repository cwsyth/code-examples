from enum import Enum


class Order(Enum):
    PRE = "preorder"
    IN = "in-order"
    POST = "post-order"
    LEVEL = "level-order"


class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

    def height(self, root):
        if root is None:
            return 0
        else:
            height_left = self.height(root.left)
            height_right = self.height(root.right)
            return max(height_left + 1, height_right + 1)

    def print(self, order, level=1):
        if order == Order.PRE:
            print(f"{self.key}", end="-")
            if self.left:
                self.left.print(order)
            if self.right:
                self.right.print(order)

        if order == Order.IN:
            if self.left:
                self.left.print(order)
            print(f"{self.key}", end="-")
            if self.right:
                self.right.print(order)

        if order == Order.POST:
            if self.left:
                self.left.print(order)
            if self.right:
                self.right.print(order)
            print(f"{self.key}", end="-")

        if order == Order.LEVEL:
            if level == 1:
                print(f"{self.key}", end="-")
            else:
                if self.left:
                    self.left.print(order, level - 1)
                if self.right:
                    self.right.print(order, level - 1)

        # interative version with queue
        if order == Order.LEVEL:
            queue = [self]
            while queue:
                node = queue.pop(0)
                print(f"{self.key}", end="-")
                if self.left:
                    queue.append(self.right)
                if self.right:
                    queue.append(self.left)
            
            

    def pretty_print(self, order):
        if order == Order.LEVEL:
            height = self.height(self)
            for i in range(1, height + 1):
                self.print(order, i)
        else:
            self.print(order)


a = BinaryTree("a")
b = BinaryTree("b")
c = BinaryTree("c")
d = BinaryTree("d")
e = BinaryTree("e")
f = BinaryTree("f")
g = BinaryTree("g")
a.left = b
a.right = c
b.right = d
c.left = e
c.right = f
f.left = g

a.print("Order.PRE")
a.print("Order.IN")
a.print("Order.POST")
a.print("Order.LEVEL")