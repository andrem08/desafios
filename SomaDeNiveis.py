# Exercício adicional
# Função para utilizar: soma_niveis_arvore()

# Nó
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Encontra o tamanho da árvore binária dado o nó raiz.
# Complexidade de tempo e espaço é de O(n)
def tamanho_arvore_rec(node):
    # Caso o nó não tenha filhos
    if (node.left is None) and (node.right is None):
        return 1

    # Verifica o tamanho dos nós dos filhos e retorna o maior
    left = right = 0
    if node.left is not None:
        left = tamanho_arvore_rec(node.left)
    if node.right is not None:
        right = tamanho_arvore_rec(node.right)
    return max(left, right) + 1


# Função recursiva que realiza a soma dos níveis
# Complexidade de tempo e espaço O(n)
def soma_niveis_rec(node, index, soma):
    # Caso o nó seja nulo
    if node is None:
        return

    # Incrementa o vetor soma, no índex do nó, pelo valor do nó e em seguida vai para os filhos.
    soma[index] = soma[index] + node.value
    soma_niveis_rec(node.left, index + 1, soma)
    soma_niveis_rec(node.right, index + 1, soma)


# Constrói um vetor soma com tamanho igual à quantidade de níveis da árvore.
# Utiliza uma função recursiva que, incrementa o valor do nó atual no vetor
# soma no mesmo índex do nível do nó, e em seguida vai para ambos os nós filhos
# recursivamente.
# Complexidade O(n)
def soma_niveis_arvore(node):
    tamanho = tamanho_arvore_rec(node)

    soma = [0 for i in range(tamanho)]

    soma_niveis_rec(node, 0, soma)
    return soma

# Usar como exemplo:
# if __name__ == '__main__':
#     no = Node(1, Node(2, Node(4, Node(8), Node(9)), Node(5)), Node(3, Node(6), Node(7)))
#     print(soma_niveis_arvore(no))
#
