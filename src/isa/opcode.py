from __future__ import annotations

from enum import StrEnum, unique


@unique
class Opcode(StrEnum):
    NOP = "nop"

    ADD = "add"
    SUB = "sub"
    MUL = "mul"
    DIV = "div"
    MOD = "mod"
    NEG = "neg"

    INC = "inc"
    DEC = "dec"

    AND = "and"
    OR = "or"
    NOT = "not"

    CMP = "cmp"

    JMP = "jmp"
    JZ = "jz"
    JNZ = "jnz"

    CALL = "call"
    RET = "ret"

    IN = "IN"
    OUT = "OUT"

    LIT = "lit"

    PUSH = "push"
    POP = "pop"
    DROP = "drop"
    DUP = "dup"
    SWAP = "swap"
    OVER = "over"

    HALT = "halt"

    def __init__(self, mnemonic: str):
        self.mnemonic = mnemonic

    def __str__(self):
        return str(self.value)

    @classmethod
    def from_string(cls, value: str):
        value = value.lower()
        for opcode in cls:
            if opcode.mnemonic == value:
                return opcode
        return None
