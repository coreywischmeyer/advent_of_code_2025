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
    def __init__(self, max_number, initial_number):
        self.initial_number = initial_number
        self.max_number = max_number
        self.validate()
        self.total_positions = max_number + 1
        self.position = self.initial_number

    def turn(self, instruction: Instruction):
        """Turn the dial."""
        if instruction.direction is 'R':
            if instruction.number + self.position > self.max_number:
                self.position = (instruction.number % self.max_number) - 1
            else: 
                self.position = instruction.number + self.position
        if instruction.direction is 'L':
            if (self.position - instruction.number) < 0:
                x = (abs(instruction.number - self.position) % self.max_number) - 1
                self.position =  self.max_number - x
            else:
                self.position = self.position - instruction.number

    def validate(self):
        if self.max_number < 0:
            raise ValueError(f"Dial's Maximum dial cannot be < 0, current value: {self.max_number}")
        if self.initial_number > self.max_number or self.initial_number < 0:
            raise ValueError(f"Dial start number {self.initial_number} is not between 0 and {self.max_number}")

if __name__ == '__main__':
    pass
