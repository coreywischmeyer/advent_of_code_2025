import pytest

from puzzle_1.puzzle_1 import Instruction


def test_instruction_left():
    x = Instruction("L1")
    assert x.direction == "L"
    assert x.number == 1


def test_instruction_right():
    x = Instruction("R110")
    assert x.direction == "R"
    assert x.number == 110


def test_instruction_error():
    with pytest.raises(ValueError):
        x = Instruction("T1000")


def test_instruction_zero_padded():
    with pytest.raises(ValueError):
        x = Instruction("R0110")
