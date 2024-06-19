from __future__ import annotations

import sys

from src.isa import (
    Data,
    DataMemory,
    InstructionMemory,
    create_data_memory,
    create_instructions_memory,
    write_data,
    write_instructions,
)
from src.translator.data_translator import get_data
from src.translator.instructions_translator import translate_code


def translate(text: str) -> tuple[InstructionMemory, DataMemory]:
    text = text.splitlines()

    # Для каждого label - массив слов из той строки, на которую указывает label
    labels2data = get_data(text)
    instructions = translate_code(text, labels2data)

    data_counter = 0
    data: list[Data] = []
    for data_for_label in labels2data.values():
        for data_cell_value in data_for_label:
            data.append(Data(data_counter, data_cell_value))
            data_counter += 1

    return create_instructions_memory(instructions), create_data_memory(data)


def main(source_file: str, target_instructions_file: str, target_data_file: str) -> None:
    with open(source_file, encoding="utf-8") as f:
        source = f.read()

    instructions, data = translate(source)

    write_data(target_data_file, data)
    write_instructions(target_instructions_file, instructions)

    source_loc = len([line for line in source.split("\n") if line.strip()])
    instructions_loc = len(instructions.values)
    print("source LoC:", source_loc, "code instr:", instructions_loc)


def start():
    assert (
        len(sys.argv) == 4
    ), "Wrong arguments: translator.py <input_file> <target_instructions_file> <target_data_file>"
    _, source_file, target_instructions_file, target_data_file = sys.argv
    main(source_file, target_instructions_file, target_data_file)


if __name__ == "__main__":
    start()
