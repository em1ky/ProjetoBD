import random

def substituir_valores_iguais(lista):
    # Crie um conjunto (set) para armazenar os valores já vistos
    valores_vistos = set()

    # Percorra a lista e verifique se um valor já foi visto
    for i in range(len(lista)):
        if lista[i] in valores_vistos:
            # Se o valor já foi visto, substitua-o por um valor aleatório diferente
            novo_valor = lista[i]
            while novo_valor in valores_vistos:
                novo_valor = random.randint(16**11, 16**12 - 1)  # Gere um número de 12 dígitos
            lista[i] = novo_valor
        else:
            # Se o valor não foi visto, adicione-o ao conjunto de valores vistos
            valores_vistos.add(lista[i])

    return lista

# Exemplo de uso
numeros = []
resultado = substituir_valores_iguais(numeros)

with open('numeros.txt', 'w') as arquivo:
    for numero in resultado:
        arquivo.write(str(numero) + '\n')

print("Números foram salvos no arquivo 'numeros.txt'")
