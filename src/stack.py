class Node:
    def __init__(self, data, prev_node):
        self.data = data
        self.prev_node = prev_node


class Stack:
    def __init__(self):
        self.content = []
        self.top = None

    def get_last_node(self):
        """Получаем последний элемент из стека"""
        return None if not self.content else self.content[-1]

    def push(self, data):
        """Добавляем элемент в стек"""
        node = Node(data, self.get_last_node())
        self.top = node
        self.content.append(node)

    def pop(self):
        """Забираем последний элемент из стека"""
        if not self.content:
            return None
        else:
            result = self.content.pop()
            self.top = result.prev_node
            return result.data
