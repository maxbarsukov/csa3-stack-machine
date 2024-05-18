from src.isa.instruction import Instruction
from src.isa.memory import InstructionMemory
from src.isa.opcode import Opcode
from src.isa.program import Program


def start():
    instr = InstructionMemory(
        [
            Instruction(Opcode.PUSH),
            Instruction(Opcode.PUSH),
            Instruction(Opcode.ADD, 2),
            Instruction(Opcode.NOP, 1),
        ]
    )
    print(Program(instr, 1))
