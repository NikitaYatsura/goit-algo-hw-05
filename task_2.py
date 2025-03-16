import re
from typing import Callable

def generator_numbers(text: str):

    numbers = re.findall(r"\s\d*\.\d*\s", text)
    for numb in numbers:
        yield float(numb)


def sum_profit(text: str, func: Callable[[str], float]):
    sum = 0
    for num in generator_numbers(text):
        sum += num
    return sum

