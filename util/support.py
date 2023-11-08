import asyncio
import functools
import time
from typing import Callable, Any


async def delay(delay_seconds: int) -> int:
    print(f'Пауза {delay_seconds} сек')
    await asyncio.sleep(delay_seconds)
    print(f'Возобновляю')
    return delay_seconds


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f'выполняется {func} с аргументами {args} {kwargs}')
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'{func} завершилась за {total:.4f} с')

        return wrapped

    return wrapper
