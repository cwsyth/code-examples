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

    def print(self, order):
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

        # recursive version
        #if order == Order.LEVEL:
        #if level == 1:
        #        print(f"{self.key}", end="-")
        #    else:
        #        if self.left:
        #            self.left.print(order, level - 1)
        #        if self.right:
        #            self.right.print(order, level - 1)

        # interative version with queue
        if order == Order.LEVEL:
            queue = [self]
            while queue:
                node = queue.pop(0)
                print(f'{node.key}', end='-')
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            

    def pretty_print(self, order):
        print(f'{order.value}: ', end='')
        self.print(order)
        print('')



class BinarySearchTree(BinaryTree):
    def __init__(self, key):
        BinaryTree.__init__(self, key)
    

    def insert(self, key):
        if self.key:
            if key < self.key:
                if self.left is None:
                    self.left = BinarySearchTree(key)
                else:
                    self.left.insert(key)
            elif key > self.key:
                if self.right is None:
                    self.right = BinarySearchTree(key)
                else:
                    self.right.insert(key)
        else:
            self.key = key


    def delete(self, key):
        if self == None:
            return self

        if key < self.key:
            self.left = self.left.delete(key)
        elif key > self.key:
            self.rigth = self.right.delete(key)
        else: # key == self.key
            if self.left == None:
                return self.right
            elif self.right == None:
                return self.left
            else:
                # inorder successor
                successor = self.right
                while successor.left:
                    successor = successor.left
                
                self.key = successor.key
                self.right = self.right.delete(successor.key)
                return self
        


tree = BinarySearchTree("d")
tree.insert("f")
tree.insert("b")
tree.insert("c")
tree.insert("a")
tree.insert("e")
tree.insert("d")
tree.insert("h")
tree.insert("g")
tree.pretty_print(Order.PRE)
tree.delete("f")
tree.pretty_print(Order.PRE)



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
a.pretty_print(Order.PRE)
a.pretty_print(Order.IN)
a.pretty_print(Order.POST)
a.pretty_print(Order.LEVEL)