from __future__ import annotations

from src.isa import Instruction, InstructionMemory, Opcode
from src.machine.components.call_stack import CallStack
from src.machine.components.data_path import DataPath


class ControlUnit:
    """Блок управления процессора. Выполняет декодирование инструкций и
    управляет состоянием модели процессора, включая обработку данных (DataPath).
    """

    program: InstructionMemory = None
    "Память команд."

    pc: int = None
    "Счётчик команд. Инициализируется нулём."

    call_stack: CallStack = None
    "Стек вызовов."

    data_path: DataPath = None
    "Блок обработки данных."

    _tick: int = None
    "Текущее модельное время процессора (в тактах). Инициализируется нулём."

    def __init__(self, program: InstructionMemory, call_stack: CallStack, data_path: DataPath):
        self.program = program
        self.pc = 0
        self.call_stack = call_stack
        self.data_path = data_path
        self._tick = 0

    def tick(self) -> None:
        """Продвинуть модельное время процессора вперёд на один такт."""
        self._tick += 1

    def current_tick(self) -> int:
        """Текущее модельное время процессора (в тактах)."""
        return self._tick

    def signal_latch_pc(self, sel_next: bool = True) -> None:
        """Защёлкнуть новое значение счётчика команд.
        Если `sel_next` равен `True`, то счётчик будет увеличен на единицу,
        иначе -- будет установлен в значение аргумента текущей инструкции.
        """
        if sel_next:
            self.pc += 1
        else:
            instr = self.program.values[self.pc]
            assert instr.operand is not None, "internal error, operand is None"
            self.pc = instr.operand

    def decode_and_execute_control_flow_instruction(self, instr: Instruction) -> bool:
        """Декодировать и выполнить инструкцию управления потоком исполнения. В
        случае успеха -- вернуть `True`, чтобы перейти к следующей инструкции.
        """
        opcode = instr.opcode

        if opcode == Opcode.HALT:
            raise StopIteration()

        sel_next = True
        if (
            opcode == Opcode.JMP
            or (opcode == Opcode.JZ and self.data_path.zero_flag)
            or (opcode == Opcode.JNZ and not self.data_path.zero_flag)
        ):
            sel_next = False
        elif opcode == Opcode.CALL:
            self.call_stack.push(self.pc + 1)
            sel_next = False
        elif opcode == Opcode.RET:
            instr.operand = self.call_stack.pop()
            sel_next = False

        if opcode in {
            Opcode.JMP,
            Opcode.JNZ,
            Opcode.JZ,
            Opcode.CALL,
            Opcode.RET,
        }:
            self.signal_latch_pc(sel_next)
            self.tick()
            return True

        return False

    def decode_and_execute_instruction(self):
        instr = self.program.values[self.pc]

        if self.decode_and_execute_control_flow_instruction(instr):
            return

        self.data_path.latch_tos(instr)
        self.signal_latch_pc()
        self.tick()

    def __repr__(self):
        state_repr = "TICK: {:3},  PC: {:3},  AR: {:3},  MEM_OUT: {:3},  TOS: {:22},".format(
            self.current_tick(),
            self.pc,
            self.data_path.data_addr,
            self.data_path.memory.memory.values[self.data_path.data_addr].value,
            str(self.data_path.stack),
        )

        instr = self.program.values[self.pc]
        instr_repr = instr.opcode + (" {}".format(instr.operand) if instr.operand is not None else "")
        return "{}    {:10}|".format(state_repr, instr_repr)
