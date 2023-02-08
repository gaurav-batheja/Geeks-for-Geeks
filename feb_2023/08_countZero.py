# Given a Matrix size N*N and an integer K. Initially, the matrix contains only 0. You are given K tasks and for each task, you are given two coordinates (r,c) [1 based index]. Where coordinates (r,c) denotes rth row and cth column of the given matrix.
# You have to perform each task sequentially in the given order. For each task, You have to put 1 in all rth row cells and all cth columns cells.
# After each task, You have to calculate the number of 0 present in the matrix and return it.
def countZero(self, n, k ,arr):
  res=[]
  mat_rows=set()
  mat_col=set()
  for i in arr:
    row,col=i
    mat_rows.add(row)
    mat_col.add(col)
    res.append((n-len(mat_rows))*(n-len(mat_col)))
  return res
