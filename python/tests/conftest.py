import numpy as np
import casm.xtal as xtal
import pytest

@pytest.fixture
def tetragonal_lattice():

    # Lattice vectors
    lattice_column_vector_matrix = np.array([
        [1., 0., 0.], # a
        [0., 1., 0.], # a
        [0., 0., 2.]] # c
        ).transpose()
    return xtal.Lattice(lattice_column_vector_matrix)


@pytest.fixture
def nonprimitive_cubic_occ_prim():

    # Lattice vectors
    lattice_column_vector_matrix = np.array([
        [1., 0., 0.], # a
        [0., 2., 0.], # a
        [0., 0., 1.]] # a
        ).transpose()
    lattice = xtal.Lattice(lattice_column_vector_matrix)

    # Basis sites positions, as columns of a matrix,
    # in fractional coordinates with respect to the lattice vectors
    coordinate_frac = np.array([
        [0., 0., 0.],
        [0., 0.5, 0.]]).transpose()

    # Occupation degrees of freedom (DoF)
    occupants = {}
    occ_dof = [
        ["A", "B"],
        ["A", "B"]
    ]

    # Local continuous degrees of freedom (DoF)
    local_dof = []

    # Global continuous degrees of freedom (DoF)
    global_dof = []

    return xtal.Prim(lattice=lattice, coordinate_frac=coordinate_frac, occ_dof=occ_dof,
                     local_dof=local_dof, global_dof=global_dof, occupants=occupants)


@pytest.fixture
def perovskite_occ_prim():

    # Lattice vectors
    lattice_column_vector_matrix = np.array([
        [1., 0., 0.], # a
        [0., 1., 0.], # a
        [0., 0., 1.]] # a
        ).transpose()
    lattice = xtal.Lattice(lattice_column_vector_matrix)

    # Basis sites positions, as columns of a matrix,
    # in fractional coordinates with respect to the lattice vectors
    coordinate_frac = np.array([
        [0., 0., 0.],
        [0.5, 0.5, 0.5],
        [0.0, 0.5, 0.5],
        [0.5, 0.0, 0.5],
        [0.5, 0.5, 0.0]]).transpose()

    # Occupation degrees of freedom (DoF)
    occupants = {}
    occ_dof = [
        ["Sr", "La"],
        ["Ti", "Nb"],
        ["O"],
        ["O"],
        ["O"]
    ]

    # Local continuous degrees of freedom (DoF)
    local_dof = []

    # Global continuous degrees of freedom (DoF)
    global_dof = []

    return xtal.Prim(lattice=lattice, coordinate_frac=coordinate_frac, occ_dof=occ_dof,
                     local_dof=local_dof, global_dof=global_dof, occupants=occupants)

@pytest.fixture
def test_nonprimitive_manydof_prim():
    # Lattice vectors
    lattice_column_vector_matrix = np.array([
        [1., 0., 0.], # a
        [0., 2., 0.], # b
        [0., 0., 1.]] # c
        ).transpose()
    lattice = xtal.Lattice(lattice_column_vector_matrix)

    # Basis sites positions, as columns of a matrix,
    # in fractional coordinates with respect to the lattice vectors
    coordinate_frac = np.array([
        [0., 0., 0.],
        [0., 1.5, 0.]]).transpose()

    # Occupation degrees of freedom (DoF)
    occupants = {
        "A.up": xtal.Occupant("A", properties={"Cmagspin": np.array([1.])}),    # A atom, spin up
        "A.down": xtal.Occupant("A", properties={"Cmagspin": np.array([-1.])})  # A atom, spin down
    }
    occ_dof = [
        ["A.up", "A.down"],
        ["A.up", "A.down"]
    ]

    # Local continuous degrees of freedom (DoF)
    disp_dof = xtal.DoFSetBasis("disp")             # Atomic displacement
    local_dof = [
        [disp_dof], # basis site 1
        [disp_dof]  # basis site 2
    ]

    # Global continuous degrees of freedom (DoF)
    GLstrain_dof = xtal.DoFSetBasis("GLstrain")     # Green-Lagrange strain metric
    global_dof = [GLstrain_dof]

    return xtal.Prim(lattice=lattice, coordinate_frac=coordinate_frac, occ_dof=occ_dof,
                     local_dof=local_dof, global_dof=global_dof, occupants=occupants)