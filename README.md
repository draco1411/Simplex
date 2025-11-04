I took a proof based class many years ago about linear programming and the simplex alg. I solved a lot by hand and proved 
some nice facts about the overall theory. It was always on my TODO list to write code that did this all for me. 
This is all done with native lists in python and does not rely on NumPy #BallOutTillTheyCrawlOut

This simple implementation used the simplex tableau (big M coming soon) to solve simple, well formulated linear optimization problems.

As such, the user needs to enter the data in tableau form with slack variables added. Given a problem like:

$$\text{MAX }7x_1 + 6x_2$$
such that
$$
2x_1 + 4x_2 + s_1 = 16
$$
$$
3x_1 + 2x_2 + s_2 = 12.
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
