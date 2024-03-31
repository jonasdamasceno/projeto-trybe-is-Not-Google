from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    priority_queue.enqueue({"qtd_linhas": 3})
    priority_queue.enqueue({"qtd_linhas": 4})
    priority_queue.enqueue({"qtd_linhas": 6})
    assert len(priority_queue) == 3
    assert len(priority_queue.high_priority) == 2
    assert len(priority_queue.regular_priority) == 1

    priority_queue.dequeue()
    assert len(priority_queue) == 2

    teste = priority_queue.search(0)
    assert teste["qtd_linhas"] == 4

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(5)