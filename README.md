This simple implementation used the simplex tableau (big M coming soon) to solve simple, well formulated linear optimization problems.
This is all done with native lists in python and does not rely on NumPy #BallOutTillTheyCrawlOut

As such, the user needs to enter the data in tableau form with slack variables added. For example, 

$$\text{Max }7x_1 + 6x_2$$
such that
$$
2x_1 + 4x_2 \leq 16
$$
$$
3x_1 + 2x_2 \leq 12.
$$

needs to be converted into "standard form" by adding slack variables to get

$$\text{Max }7x_1 + 6x_2$$
such that
$$
2x_1 + 4x_2 + s_1 \phantom{+ s_2} = 16
$$
$$
3x_1 + 2x_2 \phantom{+ s_1} + s_2 = 12.
$$

Then the variables in the USER DEFINED SECTION would be:

`max_coeff = [7, 6, 0, 0]`

`max_vars = ['x_1', 'x_2', 's_1', 's_2']`

`conditions = [[2, 4, 1, 0],
              [3, 2, 0, 1]]`

`basic_solutions = [16, 12]`

`current_basis = [0, 0]`

Note that with this form, `current_basis` will always be a zero vector. 


I've kept the session.vim file intact mostly for me. 
