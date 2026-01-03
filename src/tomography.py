import numpy as np
from numpy.linalg import svd

I = np.eye(2)
X = np.array([[0, 1], [1, 0]])
Y = np.array([[0, -1j], [1j, 0]])
Z = np.array([[1, 0], [0, -1]])

def expectation_from_counts(counts):
    return (counts[0] - counts[1]) / np.sum(counts)

def reconstructed_density_matrix(expvals):
    return 0.5 * (
        I
        + expvals["X"] * X
        + expvals["Y"] * Y
        + expvals["Z"] * Z
    )

def fidelity_pure(rho_true, rho_est):
    return np.real(np.trace(rho_true @ rho_est))

def trace_distance(rho_true, rho_est):
    svals = svd(rho_true - rho_est, compute_uv=False)
    return 0.5 * np.sum(svals)
