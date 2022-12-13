from chemistry import get_atom_radii
from typing import Union

_ratio = 0.9


def estimate_bond_length(atom1: Union[str, int], atom2: Union[str, int], bond_order: int) -> float:
    """
    calculate bond approximate length base on Pyyko radius default return is -1
    :param atom1: atom_name
    :param atom2: atom_name
    :param bond_order: bond_order
    :return: bond_length
    """
    if bond_order < 0 or bond_order > 4:
        raise
    atom1_radii = get_atom_radii(atom1)
    atom2_radii = get_atom_radii(atom2)

    if atom2_radii != -1 and atom1_radii != -1:
        length = (atom1_radii + atom2_radii) * _ratio ** (bond_order - 1)
    else:
        length = -1

    return length
