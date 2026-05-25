from typing import Protocol


class ArcaneInterface(Protocol):

    def cast(self, caster, target):
        ...

    def describe(self):
        ...


class Caster:

    def __init__(self, name, energy):

        self.name = name
        self.energy = energy

        self.artifact = None

        self.__spell_book = []

    def learn(self, spell):

        self.__spell_book.append(spell)

    def forget(self, spell_name):

        self.__spell_book = [
            s for s in self.__spell_book
            if s.name != spell_name
        ]

    def cast(self, spell_name, target):

        for spell in self.__spell_book:

            if spell.name == spell_name:
                return spell.cast(self, target)

        return "spell not found"

    def equip(self, artifact):

        if self.artifact is not None:
            print("artifact replaced")

        self.artifact = artifact

    def __len__(self):

        return len(self.__spell_book)