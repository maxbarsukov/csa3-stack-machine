from src.isa.memory import InstructionMemory


class Program:
    def __init__(self, instructions: InstructionMemory, init: int) -> None:
        self.instructions = instructions
        self.init = init

    def __eq__(self, other):
        if isinstance(other, Program):
            return self.instructions.values == other.instructions.values and self.init == other.init
        return False

    def __str__(self) -> str:
        result = ""
        for i, instr in enumerate(self.instructions.values):
            if i == self.init:
                result += f"{("> " + str(i)+"."):<8} {instr}\n"
            else:
                result += f"{("  " + str(i)+"."):<8} {instr}\n"

        return result
