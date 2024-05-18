from src.constants import MAX_NUMBER, MIN_NUMBER


class Data:
    def __init__(self, value: int) -> None:
        assert MIN_NUMBER <= value <= MAX_NUMBER, f"Value '{value}' is out of bound"
        self.value = value

    def __str__(self) -> str:
        return f"{self.value}"
