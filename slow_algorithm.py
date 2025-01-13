def fibonacci_matrix(n):
    def matrix_multiply(A, B):
        return [[A[0][0] * B[0][0] + A[0][1] * B[1][0],
                 A[0][0] * B[0][1] + A[0][1] * B[1][1]],
                [A[1][0] * B[0][0] + A[1][1] * B[1][0],
                 A[1][0] * B[0][1] + A[1][1] * B[1][1]]]

    def matrix_power(M, p):
        result = [[1, 0], [0, 1]]  
        while p:
            if p % 2:
                result = matrix_multiply(result, M)
            M = matrix_multiply(M, M)
            p //= 2
        return result

    if n <= 1:
        return n
    F = [[1, 1], [1, 0]]  
    result = matrix_power(F, n - 1)
    return result[0][0]

n = 77
print(f"Fibonacci({n}) =", fibonacci_matrix(n))

