import logging

from src.isa import Instruction, Opcode
from src.machine.components.alu import ALU
from src.machine.components.data_stack import DataStack
from src.machine.components.io import IOController
from src.machine.components.memory import Memory


def log_io(symbol: int, name: str):
    if symbol == 0:
        logging.debug("%s: \\0", name)
    elif symbol == -1:
        logging.debug("%s: EOF", name)
    elif symbol == 10:
        logging.debug("%s: \\n", name)
    else:
        try:
            logging.debug("%s: %s", name, chr(symbol))
        except ValueError:
            logging.debug("%s: %s", name, str(symbol))


class DataPath:
    """Тракт данных (пассивный), включая: ввод/вывод, память и арифметику."""

    def __init__(self, stack: DataStack, memory: Memory, io_controller: IOController):
        self.alu = ALU()
        self.stack = stack
        self.memory = memory
        self.io_controller = io_controller
        self.data_addr = 0
        self.zero_flag = False
        self.negative_flag = False

    def latch_tos(self, instr: Instruction) -> None:
        opcode = instr.opcode

        if opcode == Opcode.LOAD:
            self.latch_data_addr()
            self.stack.push(self.memory.signal_read(self.data_addr))
            self.zero_flag = self.stack.top() == 0
            self.negative_flag = self.stack.top() < 0

        elif opcode == Opcode.STORE:
            self.memory.signal_write(self.stack.pretop(), self.stack.top())

        elif opcode == Opcode.DEBUG:
            logging.debug("DEBUG: %s", repr(self))
            logging.debug("DEBUG: %s", self.memory.memory.values)
            input()

        elif opcode == Opcode.POP:
            self.stack.pop()

        elif opcode == Opcode.DUP:
            self.stack.dup()

        elif opcode == Opcode.OVER:
            self.stack.over()

        elif opcode == Opcode.OVER3:
            self.stack.over3()

        elif opcode == Opcode.SWAP:
            self.stack.swap()

        elif opcode == Opcode.CMP:
            self.stack.push(self.alu.perform(opcode, self.stack.top(), self.stack.pretop()))
            self.zero_flag = self.alu.z_flag
            self.negative_flag = self.stack.top() < 0
            self.stack.pop()

        elif opcode in {
            Opcode.ADD,
            Opcode.SUB,
            Opcode.MUL,
            Opcode.DIV,
            Opcode.MOD,
            Opcode.AND,
            Opcode.OR,
        }:
            self.stack.push(self.alu.perform(opcode, self.stack.pop(), self.stack.pop()))
            self.zero_flag = self.alu.z_flag
            self.negative_flag = self.stack.top() < 0

        elif opcode in {Opcode.INC, Opcode.DEC, Opcode.NOT, Opcode.NEG}:
            self.stack.push(self.alu.perform(opcode, self.stack.pop(), 0))
            self.zero_flag = self.alu.z_flag
            self.negative_flag = self.stack.top() < 0

        elif opcode == Opcode.INPUT:
            symbol = self.io_controller.signal_read(instr.operand)
            self.stack.push(symbol)
            log_io(symbol, "INPUT")

        elif opcode == Opcode.OUTPUT:
            symbol = self.stack.top()
            self.io_controller.signal_write(symbol, instr.operand)
            log_io(symbol, "OUTPUT")

        elif opcode == Opcode.PUSH:
            self.stack.push(instr.operand)
            self.zero_flag = self.stack.top() == 0
            self.negative_flag = self.stack.top() < 0

    def latch_data_addr(self):
        self.data_addr = self.stack.top()
