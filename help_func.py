def dotp(a, b):
    """docstring

    Dot product between vector a and b

    Args:
        a, b (list[int]): vectors of equal size

    Returns:
        dot_product (int): The dot product

    Raises:
        None
    """
    dot_product = sum([a[i]*b[i] for i in range(len(a))])
    return dot_product


def col_index(A, i):
    """docstring

    Pulls a column out of a list[list[int]] (matrix) given an index
    [[1, 2],
     [3, 4]]
    returns [1, 3] for i=0 and [2, 4] for i=1

    Args:
        A (matrix): The matrix in question
        i (int): the column in question

    Returns:
        col (vector): this is the column at index i

    Raises:
        None
    """
    col = [A[j][i] for j in range(len(A))]
    return col
