import pytest

from puzzle_1.puzzle_1 import Dial, Instruction

def test_dial_creation():
    d = Dial(100, 30)
    assert d.max_number == 99
    assert d.initial_number == 30
    assert d.total_positions == 100
    assert d.position == 30

def test_turn_dial_past_max():
    d = Dial(100, 99)
    i1 = Instruction("R1")
    d.turn(i1)
    assert d.position == 0

def test_turn_dial_below_0():
    d = Dial(100, 0)
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
    dial = Dial(100, 50)
    i1 = Instruction("L68")
    dial.turn(i1)
    assert dial.position == 82
    dial.turn(Instruction("L30"))
    assert dial.position == 52

def test_multiple_instructions_2():
        instructions = [Instruction(x) for x in ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]]
        dial = Dial(100, 50)
        print(f"The dial starts by point at {dial.position}")
        for instruction in instructions:
            dial.turn(instruction)
            print(f"The dial is rotated {instruction.instruction} to point at {dial.position}")
        assert dial.position == 32

def test_random():
    dial = Dial(100, 0)
    dial.turn(Instruction("L5"))
    assert dial.position == 95
    dial.turn(Instruction("R5"))
    assert dial.position == 0
    dial.turn(Instruction("L1"))
    assert dial.position == 99

def test_five_dial():
    d = Dial(5, 0)
    i1 = Instruction("R5")
    d.turn(i1)
    assert d.position == 0

def test_large_numbers():
    d = Dial(100, 85)
    i1 = Instruction("L685")
    d.turn(i1)
    assert d.position == 0

def test_dial_with_two_positions_left():
    dial = Dial(2, 0)
    i1 = Instruction("L2")
    dial.turn(i1)
    assert dial.position == 0

def test_dial_with_one_position():
    dial = Dial(2, 0)
    i1 = Instruction("R2")
    dial.turn(i1)
    assert dial.position == 0
