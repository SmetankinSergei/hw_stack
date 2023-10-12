class Node:
    def __init__(self, data, prev_node):
        self.data = data
        self.prev_node = prev_node


class Stack:
    def __init__(self):
        self.content = []
        self.top = None

    def get_last_node(self):
        return None if not self.content else self.content[-1]

    def push(self, data):
        node = Node(data, self.get_last_node())
        self.top = node
        self.content.append(node)
