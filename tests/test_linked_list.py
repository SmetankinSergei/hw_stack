from src.linked_list import LinkedList


def test_insert_beginning():
    ll = LinkedList()
    ll.insert_beginning({'id': 1})
    ll.insert_beginning({'id': 0})
    assert str(ll.head) == "Node({'id': 0})"


def test_insert_at_end():
    ll = LinkedList()
    ll.insert_at_end({'id': 3})
    ll.insert_at_end({'id': 4})
    assert str(ll.tail) == "Node({'id': 4})"


def test_insert_first_node():
    ll = LinkedList()
    ll.insert_at_end({'id': 3})
    assert str(ll.tail) == "Node({'id': 3})"


def test_head():
    ll = LinkedList()
    ll.insert_beginning({'id': 1})
    head = ll.head
    assert str(head) == "Node({'id': 1})"


def test_tail():
    ll = LinkedList()
    ll.insert_at_end({'id': 1})
    tail = ll.tail
    assert str(tail) == "Node({'id': 1})"
