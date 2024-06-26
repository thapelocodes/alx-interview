# 0x07. Rotate 2D Matrix

Author: Thapelo M Moumakoe

![Python](https://img.shields.io/badge/Python-%23323330.svg?style=flat&logo=python&logoColor=%221222EF) `Data Structures` `Algorithms`

For this project, the task is to implement an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. This challenge requires a good understanding of matrix manipulation and in-place operations in Python. Here are the key concepts and resources needed to grasp in order to successfully complete this project:

## Concepts Needed:

1. **Matrix Representation in Python**:
   - Uderstanding how 2D matrices are represented using lists of lists in Python.
   - Accessing and modifying elements in a 2D matrix.
2. **In-place Operations**:
   - Performing operations on data without creating a copy of the data structure.
   - the importance of minimizing space complexity by modifying the matrix in place.
3. **Matrix Transposition**:
   - Understanding the concept of transposing a matrix (swapping rows and columns).
   - Implementing matrix transposition as a step in the rotation process.
4. **Reversing Rows in a Matrix**:
   - Manipulating rows of a matrix by reversing their order as part of the rotation process.
5. **Nested Loops**:
   - Using nested loops to iterate through 2D data structures like matrices.
   - Modifying elements within nested loops to achieve the desired rotation.

## Resources:

- **Python Official Documentation**:
  - [Data Structures (list comprehensions, nested list comprehension)](https://docs.python.org/3/tutorial/datastructures.html)
  - [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- **GeeksforGeeks Articles**:
  - [Inplace rotate square matrix by 90 degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
  - [Transpose a matrix in Single line in Python](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)
- **TutorialsPoint**:
  - [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm) for basics of list manipulation in Python.

## Additional Resources

- [Mock Technical Interview](https://www.youtube.com/watch?v=yM9Xbi-MigE)

In this project it was found that the best solution is to first transpose the matrix in-place then reverse each row of the transposed matrix. The module `numpy` could have been used but it was out of the scope of this project.
