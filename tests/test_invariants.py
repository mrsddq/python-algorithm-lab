from itertools import product

import pytest

from src.dsa.queue import Queue
from src.dsa.searching import binary_search, linear_search
from src.dsa.sorting import merge_sort
from src.dsa.stack import Stack


def test_sort_and_search_against_builtin_oracles():
    for length in range(6):
        for values in product((-1, 0, 1), repeat=length):
            ordered = merge_sort(values)
            assert ordered == sorted(values)
            for target in (-2, -1, 0, 1, 2):
                index = binary_search(ordered, target)
                assert (index == -1) == (target not in ordered)
                if index != -1:
                    assert ordered[index] == target
                expected = values.index(target) if target in values else -1
                assert linear_search(values, target) == expected


def test_merge_sort_preserves_equal_key_order_with_lt_only_objects():
    class Record:
        def __init__(self, key, name):
            self.key, self.name = key, name

        def __lt__(self, other):
            return self.key < other.key

    records = [Record(2, "a"), Record(1, "b"), Record(2, "c"), Record(1, "d")]
    original = records[:]
    assert [record.name for record in merge_sort(records)] == ["b", "d", "a", "c"]
    assert records == original


def test_interleaved_queue_operations_and_reuse_after_empty():
    queue = Queue()
    queue.enqueue(None)
    queue.enqueue("a")
    assert queue.dequeue() is None
    queue.enqueue("b")
    assert [queue.dequeue(), queue.dequeue()] == ["a", "b"]
    assert queue.is_empty() and len(queue) == 0
    with pytest.raises(IndexError):
        queue.dequeue()
    queue.enqueue("reused")
    assert queue.dequeue() == "reused"


def test_stack_peek_does_not_consume_and_empty_errors():
    stack = Stack()
    for operation in (stack.peek, stack.pop):
        with pytest.raises(IndexError):
            operation()
    for value in (None, "a", "b"):
        stack.push(value)
    assert stack.peek() == "b" and len(stack) == 3
    assert [stack.pop(), stack.pop(), stack.pop()] == ["b", "a", None]
    assert stack.is_empty()
