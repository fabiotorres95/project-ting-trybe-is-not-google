from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    x = ['x', 'y', 'z']
    y = ['a', 'b', 'c', 'x', 'y', 'z']
    prio_queue = PriorityQueue()
    prio_queue.enqueue({
        'nome_do_arquivo': 'alice.txt',
        'qtd_linhas': len(y),
        'linhas_do_arquivo': y
    })

    assert len(prio_queue) == 1

    prio_queue.enqueue({
        'nome_do_arquivo': 'bob.txt',
        'qtd_linhas': len(x),
        'linhas_do_arquivo': x
    })

    assert len(prio_queue) == 2
    assert prio_queue.search(0)['nome_do_arquivo'] == 'bob.txt'

    first = prio_queue.dequeue()

    assert len(prio_queue) == 1
    assert first['nome_do_arquivo'] == 'bob.txt'
    assert prio_queue.search(0)['nome_do_arquivo'] == 'alice.txt'

    with pytest.raises(IndexError):
        prio_queue.search(1)
