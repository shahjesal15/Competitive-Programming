'''
	Fibonacci Number 
	Using binary Exponentiation and matrix multiplication
	matrix = [
		Fn   Fn-1
		Fn-1 Fn-2
	]
'''
def fibonacciNumber(n: int) -> int:
	matrix = [
		[1, 1],
		[1, 0]
	]
	power(n - 1, matrix)
	return matrix[0][0]

def power(n: int, matrix: list):
	if n == 0 or n == 1:
		return
	M = [
		[1, 1],
		[1, 0]
	]
	power(n // 2, matrix)
	multiply(matrix, matrix)
	if n & 1:
		multiply(matrix, M)

def multiply(matrix: list, M: list):
	x = matrix[0][0] * M[0][0] + matrix[0][1] * M[1][0]
	y = matrix[0][0] * M[0][1] + matrix[0][1] * M[1][1]
	z = matrix[1][0] * M[0][0] + matrix[1][1] * M[1][0]
	w = matrix[1][0] * M[0][1] + matrix[1][1] * M[1][1]

	matrix[0][0] = x
	matrix[0][1] = y
	matrix[1][0] = z
	matrix[1][1] = w

# O(log(N)) time | O(log(N)) space 
N = int(input())
print(fibonacciNumber(N))