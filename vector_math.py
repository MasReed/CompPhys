# A few functions for vector math

def dot_product(u: list, v: list) -> float:
    """Calculates the dot product of two numerical vectors represented as lists.
    Args:
        u (list): Vector of the form [u1, u2, u3, ..., u_n]
        v (list): Vector of the form [v1, v2, v3, ..., v_n]
    Returns:
        float: The dot product as a float.
    """

    if len(u) != len(v):
        raise ValueError('The two vectors must be of equal dimension.')

    return float(sum([u[i] * v[i] for i in range(len(u))]))


def cross_product(u: list, v: list) -> list:
    """Calculates the cross product of two numerical 3D vectors represented as
    lists. E.g: [1i, 2j, 3k] x [3i, 2j, 1k] = [i, j, k]
    Args:
        u (list): Vector of the form [u1, u2, u3, ..., u_n]
        v (list): Vector of the form [v1, v2, v3, ..., v_n]
    Returns:
        list: The cross product represented as a list. E.g: [i, j, k]
    """

    if len(u) != len(v):
        raise ValueError('The two vectors must be of equal dimension.')

    if len(u) != 3:
        raise ValueError('The two vectors must be three dimensional.')

    i_hat = u[1]*v[2] - u[2]*v[1]
    j_hat = u[2]*v[0] - u[0]*v[2]
    k_hat = u[0]*v[1] - u[1]*v[0]

    return [i_hat, j_hat, k_hat]


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [8, 9, 10]
