# Given a matrix of integers, rotate the middle numbers k times
# [[1,2,3],
#  [4,5,6],
#  [7,8,9]]
# Rotated 1 time:
# [[1,4,3],
#  [8,5,2],
#  [7,6,9]]
# Rotated 2 times:
# [[1,8,3],
#  [6,5,4],
#  [7,2,9]]

import copy

# Input: 3x3 matrix
# Output: String with each matrix row in its own line
def prettify(m):
  return f'{m[0]}\n{m[1]}\n{m[2]}'

# Input: matrix, m, and number of rotations, k
# Output: prettified matrix rotated k times
def matrixRotation(m, k):
  # Positions to rotate:
  # (0,1), (1,2), (2,1), (1,0)

  # Normalize the shift for any number greater than 3

  shift = k % 4

  # Build a map for each position to shift
  key = [(0,1),(1,0),(2,1),(1,2)]

  # Make a copy of the original matrix to execute the rotation
  new_matrix = copy.deepcopy(m)

  # Execute rotation using the shift variable and key
  new_matrix[0][1] = m[key[shift][0]][key[shift][1]]
  new_matrix[1][2] = m[key[shift-1][0]][key[shift-1][1]]
  new_matrix[1][0] = m[key[shift-3][0]][key[shift-3][1]]
  new_matrix[2][1] = m[key[shift-2][0]][key[shift-2][1]]

  # Return a formatted version of the matrix
  return prettify(new_matrix)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrixRotation(matrix, 12))
