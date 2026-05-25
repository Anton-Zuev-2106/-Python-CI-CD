from typing import Any


class Thread:

    def __init__(self, name, frequency, stability):

        self.__name = name
        self.frequency = frequency
        self.stability = stability

    @property
    def frequency(self):
        return self.__frequency

    @frequency.setter
    def frequency(self, value):

        if not (0.1 <= value <= 999.9):
            raise ValueError("frequency error")

        self.__frequency = value

    @property
    def stability(self):
        return self.__stability

    @stability.setter
    def stability(self, value):

        if not (0.0 <= value <= 1.0):
            raise ValueError("stability error")

        self.__stability = value

    @property
    def name(self):
        return self.__name

    def resonate(self, other):

        return (
            self.frequency * self.stability +
            other.frequency * other.stability
        )

    def __add__(self, other):

        return Thread(
            f"{self.name}+{other.name}",
            (self.frequency + other.frequency) / 2,
            (self.stability + other.stability) / 2
        )

    def __repr__(self):
        return f"Thread({self.name})"

    def __str__(self):
        return f"{self.name}: freq={self.frequency}"


class EnergyThread(Thread):

    def __init__(self, name, frequency, stability, power):

        super().__init__(name, frequency, stability)

        self.power = power

    def resonate(self, other):

        return super().resonate(other) + self.power


class FormThread(Thread):

    def __init__(self, name, frequency, stability, shape):

        super().__init__(name, frequency, stability)

        self.shape = shape


class TimeThread(Thread):

    def __init__(self, name, frequency, stability, speed):

        super().__init__(name, frequency, stability)

        self.speed = speed