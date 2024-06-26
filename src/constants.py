WORD_SIZE = 32
OPERAND_SIZE = 24
IO_PORTS = 16

STACK_CAPACITY = 2**10
CALL_STACK_CAPACITY = 2**8

MAX_NUMBER = 1 << (WORD_SIZE - 1) - 1
MIN_NUMBER = -(1 << (WORD_SIZE - 1))

MEMORY_SIZE = 1 << OPERAND_SIZE
INSTRUCTION_LIMIT = MEMORY_SIZE
