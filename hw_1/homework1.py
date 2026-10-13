# 1

def extract_coefficients(A):
    matrix = []
    for equation in A:
        coefficients = []
        for termen in equation:
            fara_litera = termen[:-1]

            if fara_litera == "":
                coefficients.append(1.0)
            elif fara_litera == "+":
                coefficients.append(1.0)
            elif fara_litera == "-":
                coefficients.append(-1.0)
            else:
                coefficients.append(float(fara_litera))

        matrix.append(coefficients)

    return matrix


A = []
B = []

with open("ecuatii.txt", 'r') as fisier:
    for line in fisier:
        elemente = line.split()
        x = elemente[0]
        y = elemente[1] + elemente[2]
        z = elemente[3] + elemente[4]
        rand = [x, y, z]
        A.append(rand)
        B.append(float(elemente[-1]))

matrice_A = extract_coefficients(A)
for rand in matrice_A:
    print(rand)
print()
for rand in B:
    print(rand)

# 2.1


def det(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1]) -
            A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0]) +
            A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))

# 2.2


def urma(A):
    return A[0][0] + A[1][1] + A[2][2]

# 2.3


def vector_norm(B):
    return (B[0]**2 + B[1]**2 + B[2]**2) ** 0.5

# 2.4


def transpusa(A):
    transpusa = []
    for i in range(len(A[0])):
        rand_nou = []
        for j in range(len(A)):
            rand_nou.append(A[j][i])
        transpusa.append(rand_nou)
    return transpusa

# 2.5


def matrix_vector_mul(A, B):
    rezultat = []
    for i in range(len(A)):
        suma = 0
        for j in range(len(B)):
            suma += A[i][j] * B[j]
        rezultat.append(suma)
    return rezultat

# 3


def replace_column(A, B, col_index):
    new_A = [rand[:] for rand in A]
    for i in range(len(A)):
        new_A[i][col_index] = B[i]
    return new_A


def solve_cramer(A, B):
    det_A = det(A)

    Ax = replace_column(A, B, 0)
    Ay = replace_column(A, B, 1)
    Az = replace_column(A, B, 2)

    x = det(Ax) / det_A
    y = det(Ay) / det_A
    z = det(Az) / det_A

    return [x, y, z]


def get_minor(A, i, j):
    minor = []
    for rand in range(3):
        if rand == i:
            continue
        minor_row = []
        for col in range(3):
            if col == j:
                continue
            minor_row.append(A[rand][col])
        minor.append(minor_row)

    return minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0]


def get_cofactor_matrix(A):
    cofactor_mat = []
    for i in range(3):
        rand = []
        for j in range(3):
            minor_det = get_minor(A, i, j)
            cofactor = ((-1) ** (i + j)) * minor_det
            rand.append(cofactor)
        cofactor_mat.append(rand)
    return cofactor_mat


def inverse_matrix(A):
    det_A = det(A)
    cofactor_mat = get_cofactor_matrix(A)

    adjugate = transpusa(cofactor_mat)

    inversa = []
    for i in range(3):
        rand_inv = []
        for j in range(3):
            rand_inv.append(adjugate[i][j] / det_A)
        inversa.append(rand_inv)
    return inversa

# 4


def solve_inversion(A, B):
    inv_A = inverse_matrix(A)
    return matrix_vector_mul(inv_A, B)
