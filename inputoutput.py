# todo: this is where we will put the gui, is placeholder
import parsing as pr


class TextBlock:
    def __init__(self, text: str):
        self.text = text


def get_input(input_type: int, input_str: str) -> tuple[int, str]:
    return input_type, input_str


def send_output(output_type: int, output_str: str) -> None:
    return
