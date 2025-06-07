from enum import Enum


class PrintColor(str, Enum):
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    RESET = "\033[0m"


class Logger:
    @staticmethod
    def log(message: str, color: PrintColor = PrintColor.RESET) -> None:
        print(f"{color.value}{message}{PrintColor.RESET.value}")

    @staticmethod
    def log_line(color: PrintColor = PrintColor.CYAN) -> None:
        print(f"{color.value}{'=' * 40}{PrintColor.RESET.value}")
