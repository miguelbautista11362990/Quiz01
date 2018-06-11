# matVec takes a matrix and a vector and returns the corresponding matrix-vector multiplication.
def matVec(matrix,vector):
  result = []
  """
  This is a function that takes a matrix and a vector as its arguments. It then multiplies each element of the corresponding matrix with the vector and returns the new updated matrix with the correct dimensions.
  """
  for i in range(len(matrix)):
    total = 0    
    for j in range(len(vector)):
      total += matrix[i][j] * vector[j]
    result.append(total)
  return result

# Above are defined variables and conditions used to compute the expected output of matVec.
# Below are 3 tests that contain different values of a matrix and a vector to test the function above matVec. Each test should be computed independently, so it can be clearly seen how the input gives us the expected output.

matrix_0 = [[1, 2],[2, 3]]
vector_0 = [8, 10]
matrix_1 = [[2, 2], [3, 3]]
vector_1 = [2,1]
matrix_2 = [[3,2], [4, 2]]
vector_2 = [5, 2]
print(matVec(matrix_0,vector_0))
#print(matVec(matrix_1, vector_1))
#print(matVec(matrix_2, vector_2))
