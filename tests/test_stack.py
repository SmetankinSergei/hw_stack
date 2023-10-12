from src.stack import Stack


def test_get_last_node():
    stack = Stack()
    assert stack.get_last_node() is None
    stack.push('data_1')
    assert stack.get_last_node().data == 'data_1'
    stack.push('data_2')
    assert stack.get_last_node().data == 'data_2'


def test_push():
    stack = Stack()
    stack.push('data_1')
    assert stack.top.data == 'data_1'


def test_pop():
    stack = Stack()
    stack.push('data_1')
    data = stack.pop()
    assert data == 'data_1'
    assert stack.content == []
    assert stack.top is None
