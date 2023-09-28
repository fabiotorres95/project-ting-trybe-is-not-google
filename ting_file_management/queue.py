from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.__len = 0

    def __len__(self):
        return self.__len__

    def enqueue(self, value):
        """Aqui irá sua implementação"""

    def dequeue(self):
        """Aqui irá sua implementação"""

    def search(self, index):
        """Aqui irá sua implementação"""
