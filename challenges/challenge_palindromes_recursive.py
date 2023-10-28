# se eu não colocar o return no primeiro if, eu não consigo capturar o true
# da linha 6, pois o resultado True retorna para a chamada da função
# imediatamente anterior, mas essa informação não é propagada para as outras chamadas recursivas.


def is_palindrome_recursive(word, low_index, high_index):
    if low_index <= high_index and word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    if low_index > high_index:
        return True
    return False
