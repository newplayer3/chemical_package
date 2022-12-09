import numpy as np
from typing import Union
from chemistry.atom.electron_configuration import get_valence_electron
from chemistry.atom.name_and_number import get_atomic_number

# hybridization {electron_domins: hybr_type}
_hybridizations = {0: 'non', 1: 's', 2: 'sp', 3: 'sp2', 4: 'sp3', 5: 'sp3d', 6: 'sp3d2', 7: 'sp3d3', 8: 'sp3d3f'}


def cubic_shape_lewis_structure(
        atom_list: Union[list[str], list[int]],
        bond_orders: list[int] = None) -> np.ndarray:
    """
    return 3*3*3 ndarray lewis structure, main atom at (2,2,2) position.
    default return is all -1 array with same size.

    inputs: atoms_list. first element is main atom.
    inputs: bond_order. bond order between atom to main atom. the first element is charge of main_atom

    outputs: cube lewis structure
    """
    cube = np.zeros(shape=(3, 3, 3), dtype=int) - 1
    if bond_orders is not None:
        if len(atom_list) != len(bond_orders):
            raise ValueError("the atom_list and bond_list have different size")

    # check input
    if len(atom_list) == 0:
        return cube
    else:
        for i in range(len(atom_list)):
            if isinstance(atom_list[i], str):
                atom_list[i] = get_atomic_number(atom_list[i])

    if bond_orders is None:
        bond_orders = [0] + [1 for _ in range(len(atom_list) - 1)]

    # collect info for main atom
    main_atom = atom_list.pop(0)
    charge = bond_orders.pop(0)
    total_bonds = sum(bond_orders)

    electron_change = 0 - charge + total_bonds
    valence_electron, _ = get_valence_electron(main_atom)


    print(valence_electron)

    return cube


if __name__ == "__main__":
    print(cubic_shape_lewis_structure(['B', 2, 3, 4, 5, 6]))
