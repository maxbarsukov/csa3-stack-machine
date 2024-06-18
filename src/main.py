from src.isa import (
    Data,
    Instruction,
    Opcode,
    create_data_memory,
    create_instructions_memory,
    read_data,
    read_instructions,
    write_data,
    write_instructions,
)


def start() -> None:
    instr = create_instructions_memory(
        [
            Instruction(0, Opcode.PUSH, 10),
            Instruction(1, Opcode.ADD, 2),
            Instruction(2, Opcode.MUL, 1),
            Instruction(10, Opcode.POP),
        ]
    )
    data = create_data_memory(
        [
            Data(0, 1),
            Data(1, 1),
            Data(2, 0),
            Data(6, 1),
            Data(10, 2),
        ]
    )
    write_instructions("i.txt", instr)
    write_data("d.txt", data)
    print(read_instructions("i.txt"))
    print(read_data("d.txt"))
