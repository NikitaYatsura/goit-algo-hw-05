from typing import Callable

def caching_fibonachi() -> Callable[[int], int]:
    
    cache = dict()
    
    def fibonachi(number: int) -> int:

        if number <= 0:
            return 0
        elif number == 1:
            return 1
        elif number in cache:
            return cache[number]
        else:
            cache[number] = fibonachi(number - 1) + fibonachi(number - 2)
            return cache[number]
    return fibonachi

number_fibonachi = caching_fibonachi()

print(number_fibonachi(10))
print(number_fibonachi(1000))
print(number_fibonachi(1000))
