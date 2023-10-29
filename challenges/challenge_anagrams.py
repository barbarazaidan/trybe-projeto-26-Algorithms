def merge_sort(string_list, start, mid, end):
    left = string_list[start:mid]  # indexando a lista da esquerda
    right = string_list[mid:end]  # indexando a lista da direita

    left_index, right_index = 0, 0  # as duas listas começarão do início

    # percorre a lista inteira como se fosse uma
    for index in range(start, end):
        # se os elementos da esquerda acabam,
        # preenche o restante com a lista da direita

        if left_index >= len(left):
            string_list[index] = right[right_index]
            right_index += 1

        # se os elementos da direita acabaram,
        # preenche o restante com a lista da esquerda
        elif right_index >= len(right):
            string_list[index] = left[left_index]
            left_index += 1

        # se o elemento do topo da esquerda for menor que o da direita,
        # ele será o escolhido
        elif left[left_index] < right[right_index]:
            string_list[index] = left[left_index]
            left_index += 1

        # caso o da direita seja menor, ele será o escolhido
        else:
            string_list[index] = right[right_index]
            right_index += 1


def order_list(list, start, end):
    if end is None:
        end = len(list)

    # se não reduzi o suficiente, continua dividindo
    if end - start > 1:
        # encotra o meio da lista
        mid = (end + start) // 2
        # ordena a lista da esquerda
        order_list(list, start, mid)
        # ordena a lista da direita
        order_list(list, mid, end)
        # junta as duas listas
        merge_sort(list, start, mid, end)


def is_anagram(first_string, second_string):
    first_list = list(first_string)
    second_list = list(second_string)
    start_list = 0
    end_first_list = len(first_list)
    end_second_list = len(second_list)

    order_list(first_list, start_list, end_first_list)
    order_list(second_list, start_list, end_second_list)

    first_string = "".join(first_list)
    second_string = "".join(second_list)

    if first_string != second_string:
        return (first_string, second_string, False)
    if first_string == "" or second_string == "":
        return (first_string, second_string, False)
    return (first_string, second_string, True)


print(is_anagram("roma", "amor"))
