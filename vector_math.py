# A few functions for vector math
from math import sqrt


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


def abs2(v: list) -> float:
    """Calculates the absolute value of a vector, v, squared.
    Args:
        v (list): Vector of the form [v1, v2, v3, ..., v_n]
    Returns:
        float: The absolute value of the vector as a float, squared.
    """
    return sum([v[i] * v[i] for i in range(len(v))])


def normalized(v: list) -> list:
    """Normalizes a vector v, such that |v|^2 = 1.
    Args:
        v (list): Vector of the form [v1, v2, v3, ..., v_n]
    Returns:
        float: The normalized vector.
    """
    return [v[i] / sqrt(abs2(v)) for i in range(len(v))]


def parse_input(s: str) -> list:
    """Parses input string to list.
    Args:
        s (str): String input of form '[v1, v2, v3, ..., v_n]'.
    Returns:
        list: Vector as list, usable by other functions.
    """
    vector_string = s.strip('[').strip(']').split(',')
    vector_list = [int(s) for s in vector_string]

    return vector_list


if __name__ == "__main__":
    # a = [1, 2, 3]
    # b = [4, 5, 6]
    # c = [8, 9, 10]
    # test_input = '[1, 2, 3]'

    input_prompt1 = 'Enter the first vector as a list. E.g. [1, 2, 3]\n'
    input_prompt2 = 'Enter the second vector as a list. E.g. [4, 5, 6]\n'

    print('[1]: Calculate dot product of two 3D vectors.')
    print('[2]: Calculate cross product of two 3D vectors.')
    print('[3]: Calculate the absolute value, squared, of a vector.')
    print('[4]: Normalize a vector')
    fxn_choice = input()

    if fxn_choice == '1':
        a = input(input_prompt1)
        b = input(input_prompt2)
        a, b = parse_input(a), parse_input(b)
        print(dot_product(a, b))

    elif fxn_choice == '2':
        a = input(input_prompt1)
        b = input(input_prompt2)
        a, b = parse_input(a), parse_input(b)
        print(cross_product(a, b))

    elif fxn_choice == '3':
        a = input(input_prompt1)
        a = parse_input(a)
        print(abs2(a))

    elif fxn_choice == '4':
        a = input(input_prompt1)
        a = parse_input(a)
        print(normalized(a))
