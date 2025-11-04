

def dotp(a, b):
    """docstring

    Dot product between vector a and b

    Args:
        a, b (list[int]): vectors of equal size

    Returns:
        integer

    Raises:
        None
    """
    return sum([a[i]*b[i] for i in range(len(a))])


def col_index(A, i):
    """docstring

    Pulls a column out of a list of lists (matrix) given a index

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


### USER DEFINED ITEMS ###
max_coeff = [7, 6, 0, 0] # with slack
max_vars = ['x_1', 'x_2', 's_1', 's_2'] # names of vars to keep track of whats leaving the basis. 

conditions = [[2, 4, 1, 0],
              [3, 2, 0, 1]]

basic_solutions = [16, 12]
current_basis = [0, 0]
### END USER DEFINED ITEMS ###


columns = [col_index(conditions, k) for k in range(len(conditions[0]))]
zj = [dotp(current_basis, columns[i]) for i in range(len(conditions[0]))]

cj_minus_zj = [max_coeff[i] - zj[i] for i in range(len(zj))]

while max(cj_minus_zj) >= 0:
    max_index = cj_minus_zj.index(max(cj_minus_zj))
    ratio_vec = 

