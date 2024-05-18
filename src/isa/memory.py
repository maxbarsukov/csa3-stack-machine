from __future__ import annotations

from typing import Generic, TypeVar

from src.constants import MEMORY_SIZE
from src.isa.data import Data
from src.isa.instruction import Instruction

MemoryType = TypeVar("MemoryType")


class Memory(Generic[MemoryType]):
    def __init__(self, values: list[MemoryType]) -> None:
        assert 1 <= len(values) <= MEMORY_SIZE, f"Out of memory for {type(values[0]).__name__}"
        self.values = values

    def __str__(self) -> str:
        return "[\n  " + ",\n  ".join(str(value) for value in self.values) + "\n]"


DataMemory = Memory[Data]
InstructionMemory = Memory[Instruction]
