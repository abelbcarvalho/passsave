# Esse arquivo possui funções para testes gerais


def is_none_empty(word='') -> bool:
    """Testa se uma string é None ou Vazia.

    Args:
        word (str, optional): palavra/frase. Defaults to ''.

    Returns:
        bool: True if it is None or Empty.
    """
    return not word or word.__len__() < 1


def is_small_equal(word='', size=25) -> bool:
    """Verifica se o tamanho de uma string é
    menor ou igual a algum inteiro enviado.

    Args:
        word (str, optional): a string. Defaults to ''.
        size (int, optional): o tamanho. Defaults to 25.

    Returns:
        bool: True se o tamanho de word é menor ou igual
        a size.
    """
    return word.__len__() <= size

def is_great_than(word='', size=25) -> bool:
    """Esse metódo verifica se uma string é
    maior do que determinado tamanho envidao.

    Args:
        word (str, optional): palavra a ser comparada. Defaults to ''.
        size (int, optional): tamanho a ser comparado. Defaults to 25.

    Returns:
        bool: True sse a palavra tem tamanho maior do que o enviado.
    """
    return word.__len__() > size


def is_equals(word='', size=25) -> bool:
    """Esse metódo verifica se uma string
    tem comprimento igual a determinado
    tamanho envidao.

    Args:
        word (str, optional): palavra a ser comparada. Defaults to ''.
        size (int, optional): tamanho a ser comparado. Defaults to 25.

    Returns:
        bool: True se a string tem tamanho igual ao enviado.
    """
    return word.__len__() == size


def is_great_equal(word='', size=25) -> bool:
    """Esse metódo verifica se uma string é
    maior ou igual a determinado tamanho envidao.

    Args:
        word (str, optional): palavra a ser comparada. Defaults to ''.
        size (int, optional): tamanho a ser comparado. Defaults to 25.

    Returns:
        bool: True -><- a palavra tem tamanho maior do que o enviado.
    """
    return word.__len__() >= size


def tira_espacos_inicio_final(word='') -> str:
    """Tira os espaços do final e do inicio de uma string.
    Exemplo:
    '    str    '
    Se torna:
    'str'

    Args:
        word (str, optional): palavra a ser mudada. Defaults to ''.

    Returns:
        str: sem espaços no final e no inicio
    """
    return word.strip() if not is_none_empty(word=word) else None


def take_space(word='') -> str:
    """Esse metódo tira todos os espaços
    de uma string.

    Args:
        word (str, optional): palavra original. Defaults to ''.

    Returns:
        str: palavra sem espaços.
    """
    return word.replace(' ', '')


def is_float_positive(point=0.0) -> bool:
    """Testa se um numero float é maior que 0.

    Args:
        point (float, optional): valor float. Defaults to 0.0.

    Returns:
        bool: True se point > 0.0.
    """
    return point > 0.00


def is_int_positive(inter=0) -> bool:
    """Verifica se um inteiro é positivo.

    Args:
        inter (int, optional): número inteiro. Defaults to 0.

    Returns:
        bool: True se inter > 0.
    """
    return inter > 0


def make_str_list_each(word='') -> list:
    """Converte uma string ume uma lista com cada
    caractere correspondendo a um indice.

    Args:
        word (str, optional): palavra a ser convertida. Defaults to ''.

    Returns:
        list: str transformado em list.
    """
    return [letra for letra in word]


def make_str_list(word=''):
    """Converte str em list.

    Args:
        word (str, optional): palavra. Defaults to ''.

    Returns:
        list: lista das letras da palavra.
    """
    return word.split()


def str_can_int_float(word='') -> bool:
    """Verifica se uma string pode ser inteiro
    se sim, pode ser float também.

    Args:
        word (str, optional): verifica se palavra
        pode ser int e float:. Defaults to ''.

    Returns:
        bool: True se palavra pode ser convertida
        em int e float.
    """
    if not isinstance(word, str):
        return False
    try:
        int(word)
        float(word)
        return True
    except ValueError:
        return False
