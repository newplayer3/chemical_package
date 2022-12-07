import closed_stable_config as csc
import numpy as np
from typing import Union


def get_charge_range(atom: Union[str, int]) -> tuple[int, int]:
    """
    return the range of possible charge for atom, default return (-1，-1)
    :param atom: str

    """
    electron_loss, electron_gain = csc.config_diff_to_reference(atom)

    max_charge = int(np.sum(electron_loss))
    min_charge = int(np.sum(electron_gain))

    return min_charge, max_charge


if __name__ == "__main__":
    print(get_charge_range('Fe'))
