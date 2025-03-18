import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:

    numbers = re.findall(r"\s\d*\.\d*\s", text)
    for numb in numbers:
        yield float(numb)


def sum_profit(text: str, func: Callable[[str], float]):
    sum = 0
    for num in func(text):
        sum += num
    return sum


