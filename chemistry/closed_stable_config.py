from atomicfeatures import get_atomic_number, get_atomic_name, get_electron_configuration_diff_by_name, \
    get_electron_configuration_diff_by_number
import numpy as np

noble_nums = [0, 2, 10, 18, 36, 54, 86, 118]


def get_ref_noble_gas_by_name(atom: str) -> tuple[str, str]:
    """
    find the closest noble atom. default return ('-1','-1')
    """
    atom_num = get_atomic_number(atom)
    for i in range(7):
        ref1 = noble_nums[i]
        ref2 = noble_nums[i + 1]
        if ref1 <= atom_num <= ref2:
            first_ref = ref1
            second_ref = ref2
            return get_atomic_name(ref1), get_atomic_name(ref2)
    return '-1', '-1'


def get_ref_noble_gas_by_number(atom: int) -> tuple[int, int]:
    """
    find the closest noble atom. default return (-1,-1)
    """
    atom_num = atom
    for i in range(7):
        ref1 = noble_nums[i]
        ref2 = noble_nums[i + 1]
        if ref1 <= atom_num <= ref2:
            first_ref = ref1
            second_ref = ref2
            return ref1, ref2
    return -1, -1


def config_diff_to_ref_noble_by_name(atom: str) -> tuple[np.ndarray, np.ndarray]:
    ref_1, ref_2 = get_ref_noble_gas_by_name(atom)
    return get_electron_configuration_diff_by_name(ref_1, atom), \
           get_electron_configuration_diff_by_name(ref_2, atom)


def config_diff_to_ref_noble_by_number(atom: int) -> tuple[np.ndarray, np.ndarray]:
    ref_1, ref_2 = get_ref_noble_gas_by_number(atom)
    return get_electron_configuration_diff_by_number(ref_1, atom), \
           get_electron_configuration_diff_by_number(ref_2, atom)


if __name__ == "__main__":
    print(get_ref_noble_gas_by_name('H'))
    print(get_ref_noble_gas_by_name('C'))
    print(get_ref_noble_gas_by_name('Ar'))
    print(get_ref_noble_gas_by_name('Hello'))
    print(get_ref_noble_gas_by_number(1))
    print(get_ref_noble_gas_by_number(18))
    print(get_ref_noble_gas_by_number(33))
    print(get_ref_noble_gas_by_number(1022))
    print(config_diff_to_ref_noble_by_name('H'))
    print(config_diff_to_ref_noble_by_name('C'))
    print(config_diff_to_ref_noble_by_name('Ar'))
    print(config_diff_to_ref_noble_by_name('Hello'))
