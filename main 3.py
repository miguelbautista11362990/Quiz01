# matVec takes a matrix and a vector and returns the corresponding matrix-vector multiplication.
def matVec(matrix,vector):
  result = []
  """
  This is a function that takes a matrix and a vector as its arguments. It then multiplies each element of the corresponding matrix with the vector and returns the new updated matrix with the correct dimensions.
  """
  for i in range(len(matrix)):
  # above in my first for loop the range of the length of the given matrix values are being computed.
    total = 0
    for j in range(len(vector)):
    # above in my second for loop the range of the length of the given values of the given vector are being computed.
      total += matrix[i][j] * vector[j]
    #the given matrix column and rows are being multiplied by the vector to obtain the expected output
    result.append(total)
    #the append statement is being used to add the total outputs to my expected result.
  return result
   # my expected result is being returned

# Above are defined variables and conditions used to compute the expected output of matVec.
# Below are 3 tests that contain different values of a matrix and a vector to test the function above matVec. Each test should be computed independently, so it can be clearly seen how the input gives us the expected output.

matrix_0 = [[1, 2],[2, 3]]
matrix_1 = [[8, 10, 12]]
matrix_2 = [[4], [5], [9]]

vector_0 = [8, 10]
vector_1 = [2, 1, 4]
vector_2 = [2]
print(matVec(matrix_0,vector_0))
#print(matVec(matrix_1, vector_1))
#print(matVec(matrix_2, vector_2))


