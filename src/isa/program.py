from src.isa.data import Data
from src.isa.instruction import Instruction
from src.isa.memory import InstructionMemory, DataMemory


class Program:
    def __init__(self, instructions: InstructionMemory, data: DataMemory) -> None:
        self._instructions = instructions
        self._data = data

    def __eq__(self, other):
        if isinstance(other, Program):
            return self.instructions() == other.instructions() and self.data() == other.data()
        return False

    def instructions(self) -> list[Instruction]:
        return self._instructions.values

    def data(self) -> list[Data]:
        return self._data.values

    def __str__(self) -> str:
        result = "DATA:\n" + str(self._data) + "\n\nINSTRUCTIONS:\n[\n"

        for instr in self.instructions():
            result += f"{("> " if instr.address == 0 else "  ") + str(instr)}\n"

        return result + "]\n"
