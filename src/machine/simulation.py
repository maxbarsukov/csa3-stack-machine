from __future__ import annotations

import logging

from src.constants import MEMORY_SIZE
from src.isa import DataMemory, InstructionMemory
from src.machine.components.call_stack import CallStack
from src.machine.components.data_stack import DataStack
from src.machine.components.io import IO0, IO1, IOController
from src.machine.components.memory import Memory
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
    io_controller = IOController()

    io_0_input = IO0(input_tokens)
    io_controller.add_io(io_0_input, 0)
    io_1_output = IO1(input_tokens)
    io_controller.add_io(io_1_output, 1)

    data_path = DataPath(DataStack(stack_capacity), Memory(data, MEMORY_SIZE), io_controller)
    control_unit = ControlUnit(instructions, CallStack(call_stack_capacity), data_path)

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

    logging.debug("memory: %s", data_path.memory.memory)

    output_buffer = data_path.io_controller.get_io(1).get_received_data()
    logging.info("output_buffer: %s", repr("".join(output_buffer)))

    return "".join(output_buffer), instr_counter, control_unit.current_tick()
