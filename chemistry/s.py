def get_atomic_bonding_structure(atom: str, bonding_atoms: dict) -> list:
    """
    construct a 3X3X3 space. target atom located at (2,2,2) position. the remaining bonding_atoms
    placing at remaining space according to target atom electron configuration.
    :param atom: atom_name
    :param bonding_atoms: {atom_name:bond_order}
    :return: [[(atom position), atom_name]]
    """