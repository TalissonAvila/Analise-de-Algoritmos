def insertionSort(a):
    for i in range(1, len(a)):
        valor = a[i]
        j = i - 1
        while j >= 0 and a[j] > valor:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = valor
    return a


# A = [90, 45, 12, 4, 3]
A = [15, 3, 20, 2, 5, 4, 9, 8]
print(f'O vetor ordenado de forma crescente é {insertionSort(A)}')
