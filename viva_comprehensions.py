from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    Take the range of 2 numbers and a parity that refers to an ODD or EVEN output and return a list of the desired
    parity in that range.
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
    Take the range of 2 numbers and a strategy and return a dict of key-value pairs with the key as the numbers in
    the range and the value as the key with the applied strategy.
    :param start: int of first key in dict (inclusive)
    :param stop: int of last key in dict (exclusive) :param strategy: function to be applied to key to determine
    value :return: dict
    """
    output = {value: strategy(value) for value in range(start, stop)}
    return output


def gen_set(val_in: str) -> Set:
    """
    Generate a set of the elements of a given string that returns the elements that appear in the string and are
     lowercase.

    :param val_in: string
    :return: set of the elements in the string that meet the given requirement, in this case being lowercase.
    """
    output = {element.upper() for element in val_in if element.islower() is True}
    return output

#
# print(gen_set('bAnAnA'))