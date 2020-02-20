"""
1*. Переписать код из homework6 используя ООП
2. Реализовать класс "очередь"
https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
- в качестве инициализации принимает размер очереди, если параметр не указан,
то очередь - бесконечная
- выдать сообщение об ошибке, если в полную очередь добавить элемент нельзя,
или из пустой очереди достать элемент
3. Реализовать класс "стек"
https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
- в качестве инициализации принимает размер стека, если параметр не указан,
то стек - бесконечный
- выдать сообщение об ошибке, если в полный стек добавить элемент нельзя,
или из пустого стека достать элемент
"""


class Stack:
    def __init__(self, stack_size=None):
        self.stack_size = stack_size
        self.stack = []
        self.last_index = 0

    def push(self, value):
        if self.stack_size is not None and self.last_index >= self.stack_size:
            raise Exception("Stack is full")
        self.stack.append(value)
        self.last_index += 1

    def pop(self):
        if self.last_index == 0:
           raise Exception("Empty stack")
        self.stack.pop()
        self.last_index -= 1

    def show_stack(self):
        print(self.stack)


class Queue:

    def __init__(self, q_size=None):
        self.q_size = q_size
        self.queue = []
        self.current_index = 0

    def enqueue(self,value):
        if self.q_size is not None and self.current_index >= self.q_size:
            raise Exception("Queue is full")
        self.queue.append(value)
        self.current_index += 1

    def dequeue(self):
        if self.current_index == 0:
            raise Exception("Empty queue")
        self.queue.pop(0)
        self.current_index -= 1

    def show_queue(self):
        print(self.queue)






if __name__=='__main__':

    new_stack = Stack(5)
    new_stack.push(1)
    new_stack.push(1)
    new_stack.push(1)
    new_stack.push(1)
    new_stack.push("asdad")
    new_stack.show_stack()
    new_stack.pop()
    new_stack.pop()
    q = Queue()
    q.enqueue(1)
    q.enqueue(1)
    q.enqueue(1)
    q.enqueue(1)
    q.enqueue(1)
    q.enqueue(1)
    q.enqueue(1)
    q.enqueue(1)
    q.enqueue(1)
    q.enqueue(1)
    q.enqueue(1)
    q.enqueue(1)
    q.enqueue('asd')
    q.enqueue(10)
    q.show_queue()
    q.dequeue()
    q.dequeue()
    q.show_queue()

    new_q = Queue(3)
    new_q.enqueue(1)
    new_q.enqueue(3)
    new_q.enqueue(14)
    new_q.show_queue()

