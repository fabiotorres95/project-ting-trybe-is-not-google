from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = list()
        self.__len = 0

    def __len__(self):
        return self.__len

    def enqueue(self, value):
        self.queue.append(value)
        self.__len += 1

    def dequeue(self):
        if self.__len == 0:
            return None

        self.__len -= 1
        return self.queue.pop(0)

    def search(self, index):
        if 0 > index or index >= self.__len:
            raise IndexError("Índice Inválido ou Inexistente")

        return self.queue[index]
