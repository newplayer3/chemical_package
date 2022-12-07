import attributes as af
import numpy as np
from typing import Union

_noble_nums = [0, 2, 10, 18, 36, 54, 86, 118]


def get_reference_atom(atom: Union[str, int]) -> tuple[int, int]:
    """
    find the closest noble atom. default return (-1, -1)
    """
    if isinstance(atom, str):
        atom_num = af.get_atomic_number(atom)
        for i in range(7):
            ref1 = _noble_nums[i]
            ref2 = _noble_nums[i + 1]
            if ref1 <= atom_num <= ref2:
                first_ref = ref1
                second_ref = ref2
                return af.get_atomic_name(ref1), af.get_atomic_name(ref2)
    else:
        atom_num = atom
        for i in range(7):
            ref1 = _noble_nums[i]
            ref2 = _noble_nums[i + 1]
            if ref1 <= atom_num <= ref2:
                first_ref = ref1
                second_ref = ref2
                return ref1, ref2
    return -1, -1


def config_diff_to_reference(atom: Union[str, int]) -> tuple[np.ndarray, np.ndarray]:
    """
    return elelctron config difference between atom and related two noble gas. default return (-1,-1)
    :param atom: str
    """
    ref_1, ref_2 = get_reference_atom(atom)
    return af.get_electron_configuration_diff(atom, ref_1), \
           af.get_electron_configuration_diff(atom, ref_2)


if __name__ == "__main__":
    print(get_reference_atom('H'))
    print(get_reference_atom(6))
    print(get_reference_atom('Ar'))
    print(get_reference_atom('Hello'))

    print(config_diff_to_reference('H'))
    print(config_diff_to_reference(1))
    print(config_diff_to_reference('Ar'))
    print(config_diff_to_reference('Hello'))
