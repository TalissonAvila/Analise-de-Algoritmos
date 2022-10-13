# codigo da Conta Inversao Bruto

def conta_inversao_bruto(vetor):
    contador = 0
    for i in range(1, len(vetor) - 1):
        for j in range(i + 1, len(vetor)):
            if vetor[i] > vetor[j]:
                contador += 1
    return contador


vetorTeste = [10, 3, 7, 13, 9, 1]
print(f'O numero de inversões é de: {conta_inversao_bruto(vetorTeste)}')
