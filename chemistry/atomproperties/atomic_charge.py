import closed_stable_config as csc
import numpy as np


def atom_charge_range_by_name(atom: str) -> tuple[int, int]:
    """
    return the range of possible charge for atom, default return (-1，-1)
    :param atom: str

    """
    electron_loss, electron_gain = csc.config_diff_to_ref_noble_by_name(atom)

    max_charge = np.sum(electron_loss)
    min_charge = np.sum(electron_gain)

    return min_charge, max_charge


def atom_charge_range_by_number(atom: int) -> tuple[int, int]:
    """
    return the range of possible charge for atom, default return (-1，-1)
    :param atom: str

    """
    electron_loss, electron_gain = csc.config_diff_to_ref_noble_by_number(atom)

    max_charge = np.sum(electron_loss)
    min_charge = np.sum(electron_gain)

    return min_charge, max_charge


if __name__ == "__main__":
    print(atom_charge_range_by_name('Fe'))
