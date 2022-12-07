import numpy as np

from closed_stable_config import config_diff_to_ref_noble_by_name, config_diff_to_ref_noble_by_number
from closed_stable_config import get_ref_noble_gas_by_name
from atomattributes import get_orbitals_by_positions
from atomattributes import get_electron_configuration_by_name, get_electron_configuration_by_number

# hybridization {electron_domins: hybr_type}
hybridizations = {0: 'non', 1: 's', 2: 'sp', 3: 'sp2', 4: 'sp3', 5: 'sp3d', 6: 'sp3d2', 7: 'sp3d3', 8: 'sp3d3f'}



def get_atom_hybridizations_by_name(atom: str) -> list:
    """
    return all possible hybridizations for atom default return is ['-1']
    """
    max_elec_loss, max_elec_gain = config_diff_to_ref_noble_by_name(atom)

    indexes_loss = np.nonzero(max_elec_loss)[0]
    indexes_gain = np.nonzero(max_elec_gain)[0]

    valence_orbital = get_orbitals_by_positions(indexes_loss)


    return []


if __name__ == "__main__":
    print(get_atom_hybridizations_by_name('N'))
