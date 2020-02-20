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


class Node:

    def __init__(self, size=None):
        self.size = size
        self.nature = []
        self.current_index = 0


class Stack(Node):

    def push(self, value):
        if self.size is not None and self.current_index >= self.size:
            raise Exception("Stack is full")
        self.nature.append(value)
        self.current_index += 1

    def pop(self):
        if self.current_index == 0:
            raise Exception("Empty stack")
        self.nature.pop()
        self.current_index -= 1


class Queue(Node):

    def enqueue(self, value):
        if self.size is not None and self.current_index >= self.size:
            raise Exception("Queue is full")
        self.nature.append(value)
        self.current_index += 1

    def dequeue(self):
        if self.current_index == 0:
            raise Exception("Empty queue")
        self.nature.pop(0)
        self.current_index -= 1


if __name__ == '__main__':
    new_stack = Stack(5)
    new_stack.push(1)
    new_stack.push(1)
    new_stack.push(1)
    new_stack.push(1)
    new_stack.push("asdad")
    new_stack.pop()
    new_stack.pop()
    print(new_stack.nature)

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
    q.dequeue()
    q.dequeue()
    print(q.nature)
    new_q = Queue(3)
    new_q.enqueue(1)
    new_q.enqueue(3)
    new_q.enqueue(14)
    new_q.dequeue()
    print(new_q.nature)
