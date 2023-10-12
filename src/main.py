from src.stack import Stack

if __name__ == '__main__':
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')
    print(stack.top.data)  # data3
    print(stack.top.prev_node.data)  # data2
    print(stack.top.prev_node.prev_node.data)  # data1
    print(stack.top.prev_node.prev_node.prev_node)  # None
    print(stack.top.prev_node.prev_node.prev_node.data)  # AttributeError
