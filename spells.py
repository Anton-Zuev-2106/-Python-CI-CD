from abc import ABC, abstractmethod
from enum import Enum


class Rarity(Enum):

    COMMON = 1
    RARE = 2
    LEGENDARY = 3


class Spell(ABC):

    def __init__(self, name, cost, rarity):

        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def cast(self, caster, target):
        pass

    @abstractmethod
    def describe(self):
        pass

    def __gt__(self, other):

        return self.rarity.value > other.rarity.value


class WeaveSpell(Spell):

    def cast(self, caster, target):

        caster.energy -= self.cost

        return f"{caster.name} creates weave with {target}"

    def describe(self):

        return "weave spell"


class CutSpell(Spell):

    def __init__(self, name, cost, rarity, severity):

        super().__init__(name, cost, rarity)

        self.severity = severity

    def cast(self, caster, target):

        caster.energy -= self.cost

        return f"{target} stability reduced"

    def describe(self):

        return "cut spell"


class BindSpell(Spell):

    def cast(self, caster, target):

        caster.energy -= self.cost

        return f"{target} binded"

    def describe(self):

        return "bind spell"


class LegendaryWeaveSpell(WeaveSpell):

    def cast(self, caster, target):

        base = super().cast(caster, target)

        return base + " with legendary power"


class CombinedSpell(Spell):

    def __init__(self, spells):

        self.spells = spells

    def cast(self, caster, target):

        result = []

        for spell in self.spells:
            result.append(spell.cast(caster, target))

        return "\n".join(result)

    def describe(self):

        return "combined spell"


print(LegendaryWeaveSpell.mro())