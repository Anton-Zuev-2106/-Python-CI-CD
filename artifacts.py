from abc import ABC, abstractmethod


class Artifact(ABC):

    def __init__(self):

        self.__durability = 100

    @abstractmethod
    def activate(self, thread):
        pass

    @property
    def durability(self):
        return self.__durability

    def reduce(self, value):

        self.__durability -= value


class CrystalCore(Artifact):

    def activate(self, thread):

        self.reduce(2)

        return thread.frequency * 1.5


class RuneMatrix(Artifact):

    def __init__(self, capacity=5):

        super().__init__()

        self.capacity = capacity

        self.threads = []

    def store(self, thread):

        if len(self.threads) < self.capacity:
            self.threads.append(thread)

    def activate(self, thread=None):

        total = 0

        for t in self.threads:
            total += t.frequency

        return total