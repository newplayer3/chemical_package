# _position_orbital {position_in_electron_config:(n,l)}
_position_orbital = {0: (1, 's'), 1: (2, 's'), 2: (2, 'p'), 3: (3, 's'), 4: (3, 'p'), 5: (4, 's'), 6: (3, 'd'),
                     7: (4, 'p'), 8: (5, 's'), 9: (4, 'd'), 10: (5, 'p'), 11: (6, 's'), 12: (4, 'f'), 13: (5, 'd'),
                     14: (6, 'p'), 15: (7, 's'), 16: (5, 'f'), 17: (6, 'd'), 18: (7, 'p')}

_orbital_position = dict(zip(_position_orbital.values(), _position_orbital.keys()))


def get_orbital_by_position(position: int) -> tuple[int, str]:
    """
    return orbital type (n,'m')  default return -1
    """
    return _position_orbital.setdefault(position, -1)


def get_position_by_orbital(orbital: tuple) -> int:
    """
    return orbital position in electron config  default return -1
    :param orbital: (int(n),str(m))
    """
    return _orbital_position.setdefault(orbital, -1)


def get_orbitals_by_positions(positions: list[int]) -> list[tuple[int, str]]:
    """
    return orbitals [(n,m)...] default return []
    :param positions:
    :return:
    """
    orbitals = []
    for position in positions:
        orbital = get_orbital_by_position(position)
        if orbital != -1:
            orbitals.append(get_orbital_by_position(position))
    return orbitals
