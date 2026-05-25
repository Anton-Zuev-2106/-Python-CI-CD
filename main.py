from threads import *
from spells import *
from artifacts import *
from caster import *


def execute_all(spells, caster, target):

    for spell in spells:

        print(spell.cast(caster, target))


varn = Caster("Варн", 200)
sel = Caster("Сел", 40)

energy_thread = EnergyThread(
    "Energy",
    100,
    0.9,
    50
)

form_thread = FormThread(
    "Form",
    50,
    0.8,
    "sphere"
)

time_thread = TimeThread(
    "Time",
    70,
    0.7,
    2
)

combined = energy_thread + form_thread

print(combined)

weave = WeaveSpell(
    "Weave",
    20,
    Rarity.COMMON
)

cut = CutSpell(
    "Cut",
    15,
    Rarity.RARE,
    5
)

bind = BindSpell(
    "Bind",
    10,
    Rarity.COMMON
)

legendary = LegendaryWeaveSpell(
    "Legend",
    40,
    Rarity.LEGENDARY
)

combo = CombinedSpell([
    weave,
    cut,
    bind
])

varn.learn(legendary)
varn.learn(combo)

sel.learn(weave)
sel.learn(bind)

varn.equip(RuneMatrix())

sel.equip(CrystalCore())

sel.equip(RuneMatrix())

print(varn.cast("Legend", "Сел"))

print(sel.cast("Weave", "Варн"))

execute_all(
    [weave, cut, bind, legendary, combo],
    varn,
    "Сел"
)

print()

print("=== REPORT ===")

print(f"{varn.name} | energy={varn.energy} | spells={len(varn)}")

print(f"{sel.name} | energy={sel.energy} | spells={len(sel)}")