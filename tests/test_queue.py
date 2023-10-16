from src.queue import Queue


def test_str():
    queue = Queue()
    assert str(queue) == ''
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')
    assert str(queue) == "data1\ndata2\ndata3"


def test_enqueue():
    queue = Queue()
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')
    assert len(queue.content) == 3
