import numpy as np

def read_matrix(filename):
    # Read in matrix data from file
    with open(filename) as f:
        lines = f.readlines()

    # Parse matrix data into a NumPy array
    n = int(np.sqrt(len(lines)))
    a = np.zeros(n**2, dtype=np.complex128)
    for i, line in enumerate(lines):
        c, d = map(float, line.strip()[1:-1].split(','))
        a[i] = complex(c, d)

    return a, n

def compute_eigenvalues(a, n):
    # Reshape array into a square matrix
    matrix = np.reshape(a, (n, n))

    # Check if matrix is Hermitian
    if not np.allclose(matrix, matrix.conj().T):
        raise ValueError("Matrix must be Hermitian.")

    # Compute eigenvalues and sort in ascending order
    eigenvalues = np.sort(np.linalg.eigvalsh(matrix))

    return eigenvalues

# Read in matrix from input file
a, n = read_matrix("../../raw_data/2as_g5Dw_Operator_22.txt")

# Compute eigenvalues
eigenvalues = compute_eigenvalues(a, n)

# Print sorted eigenvalues
print("Eigenvalues (sorted):", eigenvalues)

np.savetxt("../../data/2as_eigenvalues_22.txt",eigenvalues, delimiter="\n")
