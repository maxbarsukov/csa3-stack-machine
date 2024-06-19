from __future__ import annotations

import logging

from src.isa import DataMemory, InstructionMemory
from src.machine.control_unit import ControlUnit
from src.machine.data_path import DataPath


def simulation(
    instructions: InstructionMemory,
    data: DataMemory,
    input_tokens: list[str],
    stack_capacity: int,
    call_stack_capacity: int,
    instruction_limit: int,
) -> tuple[str, int, int]:
    data_path = DataPath(data, stack_capacity, input_tokens)
    control_unit = ControlUnit(instructions, data_path, call_stack_capacity)
    instr_counter = 0

    logging.debug("%s", control_unit)
    try:
        while instr_counter < instruction_limit:
            control_unit.decode_and_execute_instruction()
            instr_counter += 1
            logging.debug("%s", control_unit)
    except EOFError:
        logging.warning("Input buffer is empty!")
    except StopIteration:
        pass

    if instr_counter >= instruction_limit:
        logging.warning(f"Instruction limit {instruction_limit} reached!")

    output_buffer = data_path.io_ports[1]
    logging.info("output_buffer: %s", repr("".join(output_buffer)))

    return "".join(output_buffer), instr_counter, control_unit.current_tick()
