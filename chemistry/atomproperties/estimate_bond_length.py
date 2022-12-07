from games.atomproperties.atomattributes import get_atom_radii_by_number, get_atom_radii_by_name


def estimate_bond_length_by_name(atom1: str, atom2: str, bond_order: int) -> float:
    """
    calculate bond approximate length base on Pyyko radius default return is -1
    :param atom1: atom_name
    :param atom2: atom_name
    :param bond_order: bond_order
    :return: bond_length
    """
    if bond_order < 0 or bond_order > 4:
        raise
    ratio = 0.9
    atom1_radii = get_atom_radii_by_name(atom1)
    atom2_radii = get_atom_radii_by_name(atom2)

    if atom2_radii != -1 and atom1_radii != -1:
        length = (atom1_radii + atom2_radii) * ratio ** (bond_order - 1)
    else:
        length = -1

    return length


def estimate_bond_length_by_number(atom1: int, atom2: int, bond_order: int) -> float:
    """
    calculate bond approximate length base on Pyyko radius default return is -1
    :param atom1: _atomic_number
    :param atom2: _atomic_number
    :param bond_order: bond_order
    :return: bond_length
    """
    if bond_order < 0 or bond_order > 4:
        raise
    ratio = 0.9
    atom1_radii = get_atom_radii_by_number(atom1)
    atom2_radii = get_atom_radii_by_number(atom2)

    if atom2_radii != -1 and atom1_radii != -1:
        length = (atom1_radii + atom2_radii) * ratio ** (bond_order - 1)
    else:
        length = -1
    return length
