import pytest
import logging

from unittest.mock import patch, MagicMock

from threads import *
from spells import *
from artifacts import *
from caster import *



logging.basicConfig(
    filename='error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def test_thread_valid():

    t = Thread("A", 100, 0.5)

    assert t.frequency == 100


def test_thread_invalid_frequency():

    with pytest.raises(ValueError):

        Thread("A", -1, 0.5)


def test_thread_invalid_stability():

    with pytest.raises(ValueError):

        Thread("A", 100, 2)


def test_resonate():

    t1 = Thread("A", 100, 1)

    t2 = Thread("B", 50, 1)

    result = t1.resonate(t2)

    assert result == 150


def test_thread_add():

    t1 = Thread("A", 100, 1)

    t2 = Thread("B", 50, 1)

    t3 = t1 + t2

    assert isinstance(t3, Thread)


def test_spell_compare():

    s1 = WeaveSpell(
        "A",
        10,
        Rarity.COMMON
    )

    s2 = LegendaryWeaveSpell(
        "B",
        10,
        Rarity.LEGENDARY
    )

    assert s2 > s1


def test_caster_learn():

    caster = Caster("Mage", 100)

    spell = WeaveSpell(
        "Spell",
        10,
        Rarity.COMMON
    )

    caster.learn(spell)

    assert len(caster) == 1


def test_cast_spell():

    caster = Caster("Mage", 100)

    spell = WeaveSpell(
        "Spell",
        10,
        Rarity.COMMON
    )

    caster.learn(spell)

    result = caster.cast("Spell", "Enemy")

    assert "Enemy" in result


def test_artifact_activate():

    artifact = CrystalCore()

    t = Thread("A", 100, 1)

    result = artifact.activate(t)

    assert result == 150


def test_runematrix_store():

    matrix = RuneMatrix()

    t = Thread("A", 100, 1)

    matrix.store(t)

    assert len(matrix.threads) == 1


def test_combined_spell():

    caster = Caster("Mage", 100)

    s1 = WeaveSpell(
        "A",
        10,
        Rarity.COMMON
    )

    s2 = BindSpell(
        "B",
        10,
        Rarity.COMMON
    )

    combo = CombinedSpell([s1, s2])

    result = combo.cast(caster, "Enemy")

    assert "Enemy" in result


def test_logging_error():

    logger = logging.getLogger()

    file_handler = logging.FileHandler(
        "error.log",
        mode="w",
        encoding="utf-8"
    )

    logger.addHandler(file_handler)

    logger.setLevel(logging.ERROR)

    try:

        Thread("A", -1, 0.5)

    except ValueError:

        logger.error("frequency error")

    file_handler.close()

    with open("error.log", "r", encoding="utf-8") as file:

        content = file.read()

        assert "frequency error" in content

def test_mock_activate():

    with patch(
        'artifacts.CrystalCore.activate'
    ) as mock_activate:

        mock_activate.return_value = 99.9

        artifact = CrystalCore()

        result = artifact.activate(None)

        assert result == 99.9

        mock_activate.assert_called_once()


def test_magicmock():

    mock = MagicMock()

    mock.cast("Mage", "Enemy")

    mock.cast.assert_called_with(
        "Mage",
        "Enemy"
    )


def test_side_effect():

    mock = MagicMock()

    mock.activate.side_effect = Exception(
        "Boom"
    )

    with pytest.raises(Exception):

        mock.activate()