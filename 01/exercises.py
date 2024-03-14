# Exercicio 01
def max_consecutive_sum(nums):
    max_sum = float('-inf')  # Inicializamos a soma máxima com o menor valor possível
    current_sum = 0  # Inicializamos a soma atual como 0
    
    for num in nums:
        current_sum = max(num, current_sum + num)  # Atualizamos a soma atual
        max_sum = max(max_sum, current_sum)  # Atualizamos a soma máxima
        
    return max_sum

# Testes 01
def test_max_consecutive_sum():
    print(max_consecutive_sum([1, -3, 2, 1, -1]))
    print(max_consecutive_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_consecutive_sum([5, -1, -2, 3, -1, 2, -4]))
    print(max_consecutive_sum([1]))
    print(max_consecutive_sum([-1, -2, -3, -4, -5]))


# Exercício 02
def is_palindrome(word):
    # Removendo espaços em branco e convertendo para minúsculas para lidar com palavras com letras maiúsculas e minúsculas  
    word = word.replace(" ", "").lower()
    # Verificando se a palavra é igual à sua versão invertida
    return word == word[::-1]

# Testes 02
def text_is_palindrome():
    print(is_palindrome("radar"))
    print(is_palindrome("racecar"))
    print(is_palindrome("level"))
    # Testes negativos
    print(is_palindrome("python"))
    print(is_palindrome("hello"))
    print(is_palindrome("12321")) # Na verdade é um teste positivo mesmo
    print(is_palindrome("abccbaa"))


# Exercício 03
def count_increasing_subsets(nums):
    count = 0
    n = len(nums)

    # Percorre todos os elementos da lista
    for i in range(n):
        # Inicializa o tamanho do subconjunto atual como 1
        subset_size = 1
        # Verifica quantos elementos à direita podem ser incluídos no subconjunto crescente
        for j in range(i + 1, n):
            if nums[j] > nums[j - 1]:
                subset_size += 1
            else:
                break
        # Adiciona ao contador o número de subconjuntos crescentes que podem ser formados a partir deste elemento
        count += (subset_size * (subset_size + 1)) // 2

    return count

# Testes 03
def test_count_increasing_subsets():
    # Teste com lista vazia
    print(count_increasing_subsets([]))
    # Teste com uma lista de um elemento
    print(count_increasing_subsets([1]))
    # Teste com uma lista de números aleatórios
    print(count_increasing_subsets([1, 3, 2, 4]))
    # Teste com uma lista de números ordenados
    print(count_increasing_subsets([1, 2, 3, 4, 5]))
    # Teste com uma lista de números em ordem decrescente
    print(count_increasing_subsets([5, 4, 3, 2, 1]))
    # Teste com uma lista contendo números repetidos
    print(count_increasing_subsets([1, 2, 2, 3, 3, 3, 4]))


# Run the tests
if __name__ == "__main__":
    test_max_consecutive_sum()
    text_is_palindrome()
    test_count_increasing_subsets()
