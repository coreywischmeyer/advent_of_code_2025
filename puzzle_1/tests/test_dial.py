import pytest

from puzzle_1.puzzle_1 import Dial, Instruction

def test_dial_creation():
    d = Dial(99, 30)
    assert d.max_number == 99
    assert d.initial_number == 30
    assert d.total_positions == 100
    assert d.position == 30

def test_turn_dial_past_max():
    d = Dial(99, 99)
    i1 = Instruction("R1")
    d.turn(i1)
    assert d.position == 0

def test_turn_dial_below_0():
    d = Dial(99, 0)
    i1 = Instruction("L1")
    d.turn(i1)
    assert d.position == 99

def test_bad_dial_start_too_low():
    with pytest.raises(ValueError):
        Dial(99, -1)

def test_bad_dial_start_too_high():
    with pytest.raises(ValueError):
        Dial(99, 100)

def test_bad_dial_negative_max():
    with pytest.raises(ValueError):
        Dial(-99, 10)

def test_multiple_instructions():
    dial = Dial(99, 50)
    dial.turn(Instruction("L68"))
    assert dial.position == 82
    dial.turn(Instruction("L30"))
    assert dial.position == 52
