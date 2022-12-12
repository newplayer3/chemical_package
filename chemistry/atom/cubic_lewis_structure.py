import numpy as np
from typing import Union
from chemistry.atom.electron_configuration import get_valence_electron
from chemistry.atom.name_and_number import get_atomic_numbers
from chemistry.atom.orbital import get_electrons_orbital

# hybridization {electron_domins: hybr_type}
_hybridizations = {0: 'non', 1: 's', 2: 'sp', 3: 'sp2', 4: 'sp3', 5: 'sp3d', 6: 'sp3d2', 7: 'sp3d3', 8: 'sp3d3f'}
_orbital_ele_cap = {'s':2, 'p':6, 'd':10, 'f':14}


def get_cubic_structure(
        atom_list: Union[list[str], list[int]],
        elelctron_domain: int = 0, chirality = "left") -> np.ndarray:
    """
    return 3*3*3 ndarray lewis structure, main atom at (2,2,2) position.
    default return is all -1 array with same size.

    inputs: atoms_list. first element is main atom.
    inputs: electron_domain. number of electron group around atom default = 0
    inputs: chirality. chirality default is left

    outputs: cube lewis structure
    """
    cube = np.zeros(shape=(3, 3, 3), dtype=int) - 1
    # atom list check
    if len(atom_list) == 0:
        return cube
    else:
        atom_list = get_atomic_numbers(atom_list)

    main_atom = atom_list.pop(0)

    if chirality == 'left':
        main_atom = main_atom.sort()
    else:
        main_atom = main_atom.sort(reverse=True)











if __name__ == "__main__":
    print(get_cubic_structure(['Ce', 'H', ], [5]))
