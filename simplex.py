from help_func import dotp, col_index


### USER DEFINED ITEMS ###
max_coeff = [7, 6, 0, 0] # with slack
max_vars = ['x_1', 'x_2', 's_1', 's_2'] # names of vars to keep track of whats leaving the basis. 

conditions = [[2, 4, 1, 0],
              [3, 2, 0, 1]]

basic_solutions = [16, 12]
current_basis = [0, 0]
current_basis_vars = ['s_1', 's_2']
### END USER DEFINED ITEMS ###


columns_of_conditions: list = [col_index(conditions, k) for k in range(len(conditions[0]))] # Vec of columns; essentially transpose.
zj: list = [dotp(current_basis, columns_of_conditions[i]) for i in range(len(conditions[0]))]

cj_minus_zj: list = [max_coeff[i] - zj[i] for i in range(len(zj))]

while max(cj_minus_zj) > 0:
    pivot_column_index: int = cj_minus_zj.index(max(cj_minus_zj)) # This gives the index for the pivot col   0 atm
    ratio_vec: list = [basic_solutions[i] / col_index(conditions, pivot_column_index)[i] for i in range(len(basic_solutions))]
    pivot_row_index: int = ratio_vec.index(min(ratio_vec)) # 1 
    pivot_element: float = conditions[pivot_row_index][pivot_column_index] # 3.0

    # update the current_basis and current_basis_vars 
    current_basis[pivot_row_index] = max_coeff[pivot_column_index]
    current_basis_vars[pivot_row_index] = max_vars[pivot_column_index]

    # Convert pivot element to 1 and covert rest of row accordingly. This operation happens to the basic_solutions too
    conditions[pivot_row_index] = list(map(lambda x: x / pivot_element, conditions[pivot_row_index]))
    basic_solutions[pivot_row_index] = basic_solutions[pivot_row_index] / pivot_element


    # Convert the rest of the conditions matrix such that 0s appear in the rest of the pivot column. This is done with 
    # elementary row operations. 

    for i in range(len(conditions)):
        if i == pivot_row_index:
            continue
        # changing the basic solutions 
        scaled_basic_solutions = -(conditions[i][pivot_column_index] * basic_solutions[pivot_row_index]) + basic_solutions[i]
        basic_solutions[i] = scaled_basic_solutions


        # changing the main matrix
        scaled_pivot_row = list(map(lambda x: -(conditions[i][pivot_column_index]) * x, conditions[pivot_row_index]))
        added_vectors = [conditions[i][j] + scaled_pivot_row[j] for j in range(len(scaled_pivot_row))]
        conditions[i] = added_vectors

    # update zj and cj-zj

    columns_of_conditions: list = [col_index(conditions, k) for k in range(len(conditions[0]))]
    zj = [dotp(current_basis, columns_of_conditions[i]) for i in range(len(conditions[0]))]
    cj_minus_zj = [max_coeff[i] - zj[i] for i in range(len(zj))]


print("the solutions are: ")
for i in range(len(basic_solutions)):
    print(f"{current_basis_vars[i]} = {basic_solutions[i]}")

maxxxx = dotp(current_basis, basic_solutions)
print(f"giving an optimal maximum of {maxxxx}")

