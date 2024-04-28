class CircularQueue:
    def __init__(self, max_size):
        self.list = []
        self.max_size = max_size
        self.top = None
        self.start = None
        for i in range(max_size):
            self.list.append(None)

    def __str__(self):
        values = [str(x) for x in self.list]
        return ' '.join(values)

    def is_empty(self):
        for i in self.list:
            if i is not None:
                return False
            else:
                return True

    def is_full(self):
        if None in self.list:
            return False
        else:
            return True

    def enqueue(self, value):
        if self.is_empty():
            self.list[0] = value
            self.top = 0
            self.start = 0
        else:
            self.list[self.top+1] = value
            self.top += 1

    def dequeue(self):
        if self.is_empty():
            return 'list is empty'
        elif self.top == self.start == 0:
            self.top = None
            self.start = None
            self.list[0] = None
        else:
            self.list[self.start] = None
            self.start += 1







circular_queue = CircularQueue(10)
print(circular_queue)
print(circular_queue.is_empty())
circular_queue.enqueue(10)
circular_queue.enqueue(20)
circular_queue.enqueue(22)
circular_queue.enqueue(16)
circular_queue.enqueue(18)
print(circular_queue)
circular_queue.dequeue()
print(circular_queue)
print(circular_queue)