from src.isa import Instruction, Data, InstructionMemory, DataMemory, Opcode, Program, write_code, read_code

def start() -> None:
    instr = InstructionMemory(
        [
            Instruction(10, Opcode.PUSH),
            Instruction(0, Opcode.PUSH),
            Instruction(1, Opcode.ADD, 2),
            Instruction(2, Opcode.NOP, 1),
        ]
    )
    data = DataMemory(
        [
            Data(10, 2),
            Data(0, 10),
            Data(1, 1),
            Data(6, 1),
            Data(2, 0),
        ]
    )
    write_code("i.txt", "d.txt", Program(instr, data))
    print(read_code("i.txt", "d.txt"))
