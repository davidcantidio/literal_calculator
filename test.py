import os
import operator
# Dicionário para unidades
digitos = {
    'unidades': {
        'zero': 0,
        'um': 1,
        'dois': 2,
        'três': 3,
        'quatro': 4,
        'cinco': 5,
        'seis': 6,
        'sete': 7,
        'oito': 8,
        'nove': 9,
        
    },
    'dezenas': {
        'dez': 1,
        'vinte': 2,
        'trinta': 3,
        'quarenta': 4,
        'cinquenta': 5,
        'sessenta': 6,
        'setenta': 7,
        'oitenta': 8,
        'noventa': 9,
    },
    'centenas': {
        'cento': 1,
        'duzentos': 2,
        'trezentos': 3,
        'quatrocentos': 4,
        'quinhentos': 5,
        'seiscentos': 6,
        'setecentos': 7,
        'oitocentos': 8,
        'novecentos': 9
    }}
non_algarisms = ['milion', 'mil']


operators = {'vezes': operator.add,
             'menos': operator.sub,
             'vezes': operator.mul,
             'dividido por': operator.truediv}


operation = 'dois milhões duzentos e quinze vezes dois'

def get_operation_elements(operation, operators):
    for o in operators:
        return operation.split(" {} ".format(o))
    
get_operation_elements = get_operation_elements(operation=operation, operators=operators)

def get_operator(operation, operators):
    for o in operators:
        if o in operation:
            return operation[o]

first_element = get_operation_elements[0]
second_element = get_operation_elements[1]
operator = get_operator(operation=operation, operators=operators)


def check_teens (algarismo):
    teens_dict = {
    'onze': ['dez', 'um'],
    'doze': ['dez', 'dois'],
    'treze': ['dez', 'três'],
    'catorze': ['dez', 'quatro'],
    'quinze': ['dez', 'cinco'],
    'dezesseis': ['dez', 'seis'],
    'dezessete': ['dez', 'sete'],
    'dezoito': ['dez', 'oito'],
    'dezenove': ['dez', 'nove']
}

    if algarismo in teens_dict:
        return teens_dict[algarismo]
    return algarismo


def gen_lista_numeros(client_input):
    if client_input.startswith('mil '):
        client_input = client_input.replace('mil','um mil')
    clean_string = client_input.replace('milhões', 'milion').replace('milhão', 'milion').replace('e ', '').strip().lower()
    lista = list(map(check_teens, clean_string.split(' ')))
    lista_achatada = [item for sublist in lista for item in (sublist if isinstance(sublist, list) else [sublist])]

    return lista_achatada


def get_n_digits(lista_numeros):
    if 'milion' in lista_numeros:
        n_digits = 7 + (lista_numeros.index('milion') -1)
    elif 'mil' in lista_numeros:
        n_digits = 3 + (lista_numeros.index('mil') -1)
    return n_digits


def get_list_algarisms(lista_numeros, non_algarisms):
    return  [i for i in lista_numeros if i not in non_algarisms]


def get_n_algarisms(lista_numeros):
    return sum(1 for i in lista_numeros if i not in non_algarisms)


def fill_zeros(n_digits, n_algarisms, list_algarisms):
    l = [list_algarisms[0]]     
    list_algarisms.remove(l[0])
    n_zeros = n_digits - n_algarisms
    for i in range (0, n_zeros):
        l.append('zero')
    for n in list_algarisms:
        l.append(n)
    return l


def gen_integer_list(zero_filled_list, digitos):
    l = []
    for number_name in zero_filled_list:
        for grandeza in digitos:
            if number_name in digitos[grandeza]:
                l.append(digitos[grandeza][number_name])
                break  # Para não buscar nas outras categorias depois de encontrar
    return l

def gen_integer_number (integer_list):
   return int(''.join(map(str, integer_list)))

if __name__ == "__main__":
    
    lista_numeros = gen_lista_numeros(client_input=client_input)
    n_digits = get_n_digits(lista_numeros=lista_numeros)
    list_algarisms = get_list_algarisms(lista_numeros=lista_numeros, non_algarisms=non_algarisms)
    n_algarisms = get_n_algarisms(lista_numeros=lista_numeros)
    zero_filled_list = fill_zeros(n_digits=n_digits, n_algarisms=n_algarisms, list_algarisms=list_algarisms)
    integer_list = gen_integer_list(zero_filled_list=zero_filled_list, digitos=digitos)
    integer_number = gen_integer_number(integer_list=integer_list)
    print(integer_number)
