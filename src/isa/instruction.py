from __future__ import annotations

from src.isa.opcode import Opcode


class Instruction:
    def __init__(self, opcode: Opcode, operand: int | None = None) -> None:
        self.opcode = opcode
        self.operand = operand

    def __str__(self) -> str:
        return f"{self.opcode.name:<6} " + (f"{self.operand}" if self.operand is not None else "")
