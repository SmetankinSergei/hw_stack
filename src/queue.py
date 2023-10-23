class Queue:
    def __init__(self):
        self.content = []
        self.head = None
        self.tail = None

    def __str__(self):
        """Строковое определение объекта"""
        result = [node.data for node in self.content]
        result = '\n'.join(result)
        return result

    def enqueue(self, data):
        """Добавление элемента в очередь"""
        new_node = Node(data, None)
        self.content.append(new_node)
        if len(self.content) > 1:
            self.tail.next_node = new_node
        self.tail = new_node
        self.head = self.content[0]

    def dequeue(self):
        if self.content:
            return self.content.pop(0).data


class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f'{__class__.__name__}({self.data})'
