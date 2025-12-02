class Instruction:
    """Instruction to give to the Dial."""

    def __init__(self, instruction: str):
        self.instruction = instruction
        self.validate()
        self.direction = str(instruction[0])
        self.number = int(instruction[1:])

    def validate(self):
        """Check if instruction is valid."""
        if self.instruction[0] not in ["L", "R"]:
            raise ValueError(f"{self.instruction} direction is not valid")
        if not self.instruction[1:].isnumeric():
            raise ValueError(f"{self.instruction} number is not valid")
        if self.instruction[1] == "0":
            raise ValueError(f"{self.instruction} not allowing zero-padded numbers")

class Dial:
    """Dial."""
    def __init__(self, dial_positions, initial_number):
        self.initial_number = initial_number
        self.max_number = dial_positions - 1
        self.validate()
        self.total_positions = dial_positions
        self.position = self.initial_number

    def turn(self, instruction: Instruction):
        """Turn the dial."""
        if instruction.direction == 'R':
            if instruction.number + self.position > self.max_number:
                self.position = (instruction.number + self.position) % self.total_positions
            else:
                self.position = instruction.number + self.position
        if instruction.direction == 'L':
            if (self.position - instruction.number) < 0:
                x = (((instruction.number - self.position) % self.total_positions))
                if x == 0:
                    self.position = x
                else:
                    self.position = self.total_positions - x
            else:
                self.position = self.position - instruction.number

    def validate(self):
        if self.max_number < 0:
            raise ValueError(f"Dial's Maximum dial cannot be < 0, current value: {self.max_number}")
        if self.initial_number > self.max_number or self.initial_number < 0:
            raise ValueError(f"Dial start number {self.initial_number} is not between 0 and {self.max_number}")

if __name__ == '__main__':
    with open('data/puzzle_1.input.txt', 'r') as f:
        instructions = [Instruction(x.strip()) for x in f.readlines()]
    d = Dial(100, 50)
    zero_count = 0
    instruction_num = 0
    for instruction in instructions:
        instruction_num += 1
        d.turn(instruction)
        print(f"{instruction_num}: The dial is rotated {instruction.instruction} to point at {d.position}")
        if d.position == 0:
            zero_count += 1
    print(zero_count)
