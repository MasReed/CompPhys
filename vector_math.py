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

    return float((sum([u[i] * v[i] for i in range(len(u))]))






if __name__ == '__main__':

    a=[1, 2, 3]
    b=[3, 2, 1]
    # a dot b should = 10
