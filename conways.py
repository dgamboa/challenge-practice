# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

# _ _ _
# _ x x
# _ x x

arr = [[0, 0, 0],
       [1, 1, 1],
       [0, 0, 0]]

def nextCycle(a):
  b = [row[:] for row in a]

  for i in range(len(a)):
    for j in range(len(a[0])):
      counter = 0

      if i != 0 and a[i - 1][j] == 1:
        counter += 1

      if i != len(a) - 1 and a[i + 1][j] == 1:
        counter += 1
      
      if j != 0 and a[i][j - 1] == 1:
        counter += 1
      
      if j != len(a) - 1 and a[i][j + 1] == 1:
        counter += 1

      if i != 0 and j != 0 and a[i - 1][j - 1] == 1:
        counter += 1
      
      if i != 0 and j != len(a[0]) - 1 and a[i - 1][j + 1] == 1:
        counter += 1
      
      if i != len(a) - 1 and j != 0 and a[i + 1][j - 1] == 1:
        counter += 1
      
      if i != len(a) - 1 and j != len(a[0]) - 1 and a[i + 1][j + 1] == 1:
        counter += 1
  
      if ((counter == 2 or counter == 3) and a[i][j] == 1):
        b[i][j] = 1
      if counter < 2 and a[i][j] == 1:
        b[i][j] = 0
      elif counter > 3 and a[i][j] == 1:
        b[i][j] = 0
      if counter == 3 and a[i][j] == 0:
        b[i][j] = 1
  
  return b

c = nextCycle(arr)
d = nextCycle(c)
print(arr)
print(c)
print(d)
