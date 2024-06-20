from __future__ import annotations

import argparse
import logging

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
    parser = argparse.ArgumentParser(description='CSA Lab 3 machine runner.')
    parser.add_argument('instructions_file', type=str, help='File with instructions')
    parser.add_argument('data_file', type=str, help='File with data')
    parser.add_argument('input_file', type=str, help='File with user input')
    parser.add_argument(
        '--log_level',
        type=str,
        default='',
        choices=['FATAL', 'ERROR', 'WARN', 'INFO', 'DEBUG', 'NOTSET', ''],
        help='Log level [FATAL, ERROR, WARN, INFO, DEBUG, NOTSET]'
    )
    parser.add_argument(
        '--output_ports',
        type=str,
        default='1, 2',
        choices=['1', '2', '1;2'],
        help="IO ports to print output ['1', '2', '1;2']"
    )

    args = parser.parse_args()

    if args.log_level == 'FATAL':
        level = logging.FATAL
    elif args.log_level == 'ERROR':
        level = logging.ERROR
    elif args.log_level == 'WARN':
        level = logging.WARN
    elif args.log_level == 'INFO':
        level = logging.INFO
    elif args.log_level == 'DEBUG':
        level = logging.DEBUG
    else:
        level = logging.NOTSET

    if args.output_ports == '1':
        ports = [1]
    elif args.output_ports == '2':
        ports = [2]
    else:
        ports = [1, 2]

    logging.getLogger().setLevel(level)
    main(args.instructions_file, args.data_file, args.input_file, ports)


if __name__ == "__main__":
    start()
