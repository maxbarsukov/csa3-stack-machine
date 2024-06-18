import json
from src.constants import MAX_NUMBER, MIN_NUMBER, MEMORY_SIZE


class Data:
    def __init__(self, address: int, value: int) -> None:
        assert MIN_NUMBER <= value <= MAX_NUMBER, f"Data value '{value}' at {address} is out of bound"
        assert 0 <= address <= MEMORY_SIZE, f"Data value '{value}' is out of memory at {address}"
        self.address = address
        self.value = value

    def __str__(self) -> str:
        return f"{(str(self.address) + ":"):<6} {self.value}"

    def to_json(self) -> str:
        return json.dumps(
            self,
            default=vars,
            sort_keys=True,
            indent=2
        )
