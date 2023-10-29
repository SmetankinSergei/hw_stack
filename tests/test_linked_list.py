import pytest

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
    assert str(ll.head) == "Node({'id': 3})"
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


def test_to_list():
    ll = LinkedList()
    ll.insert_beginning({'id': 0, 'username': 'serebro'})
    ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
    ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
    assert ll.to_list()[0] == {'id': 0, 'username': 'serebro'}
    assert ll.to_list()[1] == {'id': 1, 'username': 'lazzy508509'}
    assert ll.to_list()[2] == {'id': 2, 'username': 'mik.roz'}
    assert ll.to_list()[3] == {'id': 3, 'username': 'mosh_s'}


def test_get_data_by_id():
    ll = LinkedList()
    ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    ll.insert_at_end('idusername')
    ll.insert_at_end([1, 2, 3])
    ll.insert_at_end({'id': 2, 'username': 'mosh_s'})
    assert ll.get_data_by_id(1) == {'id': 1, 'username': 'lazzy508509'}
    with pytest.raises(TypeError):
        ll.get_data_by_id(2)

