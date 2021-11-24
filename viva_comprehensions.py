from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param start: int of first value in list range (inclusive)
    :param stop: int of last value in list range (exclusive)
    :param parity: from enum class to determine ODD or EVEN
    :return: list
    """
    if parity is Parity.ODD:
        output = [value for value in range(start, stop) if value % 2 == 1]
    else:
        output = [value for value in range(start, stop) if value % 2 == 0]
    return output


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.


    :param start: int of first key in dict (inclusive)
    :param stop: int of last key in dict (exclusive)
    :param strategy: function to be applied to key to determine value
    :return: dict
    """
    output = {value: strategy(value) for value in range(start, stop)}
    return output


def gen_set(val_in: str) -> Set:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param val_in:
    :return:
    """
    pass
