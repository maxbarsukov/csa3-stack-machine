from __future__ import annotations

import logging
import sys

from src.constants import CALL_STACK_CAPACITY, INSTRUCTION_LIMIT, STACK_CAPACITY
from src.isa import read_data, read_instructions
from src.machine.simulation import simulation


def main(instructions_file: str, data_file: str, input_file: str, output_from_ports: list[int]) -> None:
    instructions = read_instructions(instructions_file)
    data = read_data(data_file)

    with open(input_file, encoding="utf-8") as f:
        input_token = [char for char in f.read()]

    output, instr_counter, ticks = simulation(
        instructions,
        data,
        input_token,
        STACK_CAPACITY,
        CALL_STACK_CAPACITY,
        INSTRUCTION_LIMIT,
        output_from_ports,
    )

    print("".join(output))
    print("instr_counter: ", instr_counter, "ticks:", ticks)


def start() -> None:
    logging.getLogger().setLevel(logging.DEBUG)
    assert len(sys.argv) == 4, "Wrong arguments: machine.py <data_file> <code_file> <input_file>"
    _, instructions_file, data_file, input_file = sys.argv
    main(instructions_file, data_file, input_file, [1, 2])


if __name__ == "__main__":
    start()
