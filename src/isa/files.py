import json
from typing import Tuple

from src.isa.memory import InstructionMemory, DataMemory
from src.isa.instruction import Instruction
from src.isa.data import Data
from src.isa.opcode import Opcode
from src.isa.program import Program


def code_to_json(program: Program) -> Tuple[str, str]:
    """Перевести машинный код в JSON."""
    buf_i = []
    for instr in program.instructions():
        buf_i.append(instr.to_json())
    instructions = "[\n" + ",\n".join(buf_i) + "\n]"

    buf_d = []
    for d in program.data():
        buf_d.append(d.to_json())
    data = "[\n" + ",\n".join(buf_d) + "\n]"

    return instructions, data


def json_to_code(instructions_json: str, data_json: str) -> Program:
    """Перевести JSON в машинный код."""
    instructions_code = json.loads(instructions_json)
    instructions = []
    for i in instructions_code:
        instructions.append(Instruction(i["address"], Opcode(i["opcode"]), i["operand"]))

    data_code = json.loads(data_json)
    data = []
    for d in data_code:
        data.append(Data(d["address"], d["value"]))

    return Program(InstructionMemory(instructions), DataMemory(data))


def write_code(instructions_filename: str, data_filename: str, program: Program) -> None:
    """Записать машинный код в файл."""
    instructions, data = code_to_json(program)

    with open(instructions_filename, "w", encoding="utf-8") as instructions_file:
        instructions_file.write(instructions)
    with open(data_filename, "w", encoding="utf-8") as data_file:
        data_file.write(data)


def read_code(instructions_filename: str, data_filename: str) -> Program:
    """Прочесть машинный код из файла."""
    with open(instructions_filename, encoding="utf-8") as instructions_file:
        instructions_json = instructions_file.read()

    with open(data_filename, encoding="utf-8") as data_file:
        data_json = data_file.read()

    return json_to_code(instructions_json, data_json)
