# Queue Operations - Create Queue, Enqueue, Dequeue, Peek, isEmpty, isFull, deleteQueue

class CustomQueue:
    def __init__(self):
        self.list = []
        self.length = 0

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return ' '.join(values)


    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def enqueue(self, value):
        self.list.append(value)
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            return 'Empty List'
        else:
            self.list.remove(self.list[0])

    def peek(self):
        if self.is_empty():
            return 'Empty list'
        else:
            return self.list[0]


new_queue = CustomQueue()
print(new_queue.is_empty())
new_queue.enqueue(10)
new_queue.enqueue(22)
print(new_queue.peek())
print(new_queue)





