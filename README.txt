Matrix Determinant Algorithms
Levi Sweat

This repository contains python code for computing the determinant of an nxn matrix using Cofactor
Expansion, PLU Factorization, and Bareiss Algorithm. The algorithms can be found in the file
src/user_matrix.py, which allows the user to input a specified matrix or randomly generate a
matrix. src/runtime_caclculations.py is a file used when calculating the runtime of computing 
determinants for large matrices. algo_completion_times.csv gives a variety of runtimes
for calculating determinants of large matrices, which is used in 
src/determinant_runtime_visualization.ipynb to visualize the Big O computing time for each
algorithm. The sources folder contains some PDFs of sources used in completing this project.