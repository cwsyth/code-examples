import sys


class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [None] * (maxsize + 1)
        self.heap[0] = sys.maxsize
        self.ROOT = 1
    

    def parent(self, pos):
        return pos // 2


    def left_child(self, pos):
        return 2 * pos


    def right_child(self, pos):
        return 2 * pos + 1
    

    def swap(self, pos_a, pos_b):
        self.heap[pos_a], self.heap[pos_b] = self.heap[pos_b], self.heap[pos_a] 


    def upheap(self, pos):
        current = pos
        while self.heap[current] > self.heap[self.parent(current)]: # update parent
            self.swap(self.parent(current), current)
            current = self.parent(current)


    def is_leaf(self, pos):
        if pos > self.size // 2 and pos <= self.size:
            return True
        return False


    def downheap(self, pos):
        if not self.is_leaf(pos):
            key = self.heap[pos]
            left_pos = self.left_child(pos)
            left_key = self.heap[left_pos]
            right_pos = self.right_child(pos)
            right_key = self.heap[right_pos]

            if key < left_key or key < right_key:
                if left_key < right_key:
                    self.swap(pos, right_pos)
                    self.downheap(right_pos)
                else:
                    self.swap(pos, left_key)
                    self.downheap(left_pos)

    def insert(self, key):
        self.size += 1
        self.heap[self.size] = key
        self.upheap(self.size)


    def extract(self):
        max_val = self.heap[self.ROOT]
        self.heap[self.ROOT] = self.heap[self.size]
        self.size -= 1
        self.downheap(self.ROOT)
        return max_val


heap = MaxHeap(33)
heap.insert(4)
heap.insert(1)
heap.insert(5)
heap.insert(10)
heap.insert(7)
heap.insert(8)
heap.insert(3)
print(heap.heap)
heap.extract()
print(heap.heap)