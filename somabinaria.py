A = [1, 1, 1, 1, 0]  # 30
B = [1, 1, 1, 1, 0]  # 30
n = 5


# C[X, 1, 1, 1, 0]
def soma_binary_integers(A, B, n):
    C = [0] * (n + 1)
    carry = 0
    i = n - 1
    while i >= 0:
        soma = A[i] + B[i] + carry
        if soma == 3:
            carry = 1
            C[i + 1] = 1
        if soma == 2:
            carry = 1
            C[i + 1] = 0
        if soma == 1:
            carry = 0
            C[i + 1] = 1
        if soma == 0:
            carry = 0
            C[i + 1] = 0
        i = i - 1
    C[0] = carry
    return C


print(soma_binary_integers(A, B, n))
