import numpy as np
from typing import Union

from closed_stable_config import config_diff_to_reference
from closed_stable_config import get_reference_atom
from attributes import get_orbitals_by_positions
from attributes import get_electron_configuration

# hybridization {electron_domins: hybr_type}
_hybridizations = {0: 'non', 1: 's', 2: 'sp', 3: 'sp2', 4: 'sp3', 5: 'sp3d', 6: 'sp3d2', 7: 'sp3d3', 8: 'sp3d3f'}


def cubic_shape_lewis_structure(
        atom_list: Union[list[str], list[int]],
        bond_orders: list[int] = None) -> np.ndarray:
    """
    return 3*3*3 ndarray lewis structure, main atom at (2,2,2) position. default return is all zero array.

    inputs: atoms_list. first element is main atom.
    inputs: bond_order. bond order between atom to main atom.

    outputs: cube lewis structure
    """
    cube = np.zeros(shape=(3, 3, 3), dtype=int)
    if len(atom_list) == 0:
        return cube
    if bond_orders is None:
        bond_orders = [0] + [1 for _ in range(len(atom_list) - 1)]



    main_atom = atom_list.pop(0)


if __name__ == "__main__":
    print(cubic_shape_lewis_structure([1, 2, 3, 4, 5, 6]))
