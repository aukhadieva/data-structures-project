"""Здесь тесты с использованием pytest для модуля stack."""
import pytest
from src.stack import Node, Stack


@pytest.fixture
def items_for_node():
    return Node(5, 0)


def test_set_next(items_for_node):
    items_for_node.set_next(1)
    assert items_for_node.next_node == 1


@pytest.fixture
def items_for_stack():
    return Stack()


def test_push(items_for_stack):
    items_for_stack.push('data1')
    items_for_stack.push('data2')
    assert items_for_stack.top.data == 'data2'
    assert items_for_stack.top.next_node.data == 'data1'


def test_pop(items_for_stack):
    items_for_stack.top = ['data1', 'data2']
    assert items_for_stack.pop() == 'data2'
    assert items_for_stack.pop() == 'data1'
    assert items_for_stack.pop() is None
