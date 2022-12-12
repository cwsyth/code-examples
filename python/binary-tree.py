import pydot

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

    
    def write_graph(self, name):
        graph = pydot.Dot(graph_type='graph')

        def traverse(node):
            if node:
                graph.add_node(pydot.Node(node.key))
                if node.left:
                    graph.add_edge(pydot.Edge(node.key, node.left.key))
                    traverse(node.left)
                if node.right:
                    graph.add_edge(pydot.Edge(node.key, node.right.key))
                    traverse(node.right)

        traverse(self)
        graph.write_pdf(name)    



class BinarySearchTree(BinaryTree):
    # __init__ gets inherited from BinaryTree
    #def __init__(self, key):
    #    BinaryTree.__init__(self, key)
    

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

        # recursively rebuild the tree, descending to the left or right subtree
        if key < self.key:
            self.left = self.left.delete(key)
            return self
        elif key > self.key:
            self.right = self.right.delete(key)
            return self
        else: # key == self.key:
            if self.left == None:
                # delete node with 0 or 1 child
                return self.right
            elif self.right == None:
                # delete node with 1 child
                return self.left
            else:
                # delete node with 2 children
                # replace the node with its inorder successor
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