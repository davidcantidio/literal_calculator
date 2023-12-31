import os
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
        'noventa': 9
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




client_input = 'dois milhões novecentos e trinta e um mil duzentos e quinze'.strip().lower().replace('milhões', 'milion')

def gen_frase_numerica(client_input):
    if client_input.startswith('mil '):
        return client_input.replace('mil','um')
    return client_input

def check_teens (algarismo, teens_dict):
    if algarismo in teens_dict:
        return teens_dict[string]


frase_numerica = gen_frase_numerica(client_input=client_input)

def gen_string_list(frase_numerica):
    frase_numerica.split(" ").
    
string_list = frase_numerica.split(" ")
string = map(check_teens, string_list)
string = string.split(" e ")
milhar = [item.split('mil ') for item in string]
milion = [item.split('milion ') for sublist in milhar for item in sublist]
milion_trimmed = [item.split() for sublist in milion for item in sublist]
list_string_numbers_raw = [valor for item in milion_trimmed for valor in item]

list_lenght = len(list_string_numbers_raw)
i = -3
list_string_numbers_raw[i:]


def translate_teens (string, teens_dict):
    if string in teens_dict:
        return teens_dict[string]


def fill_zeros(list_string_numbers_raw, lenght):
    for i in range(1, lenght):
        list_string_numbers_raw.insert(0, 'zero')
        i =+ 1
    


def compose_list_numbers(list_string_numbers_raw):
    
    if list_lenght < 3: 
        fill_zeros(list_string_numbers_raw, list_lenght)
        return list_string_numbers_raw
    
    list.pop()
    
    

#pegar lista list_string_numbers_raw 
# dividir o lenght dela por 3
    # se for 0.33
# rodar compose_list_numbers e obter sublista com 3 itens.
#remover os ultimos itens da lista original
#o


def get_last_3_numbers(list_string_numbers_raw, digitos):
    l = []
    unidade_str = list_string_numbers_raw[-1]
    dezena_str = list_string_numbers_raw[-2]
    centena_str = list_string_numbers_raw[-3]
        
    if unidade_str in digitos['unidades']:
        unidade = digitos['unidades'][unidade_str]
        if dezena_str in digitos['dezenas']:
            dezena = digitos['dezenas'][dezena_str]
        if dezena_str in digitos['centenas']:
            dezena = 0
            centena = digitos['centenas'][dezena_str]
    elif unidade_str in digitos['dezenas']:
        unidade = digitos['dezenas'][dezena_str]
        dezena = 1
    elif unidade_str in digitos['centenas']:
        unidade = 0
        dezena = 0
        centena = digitos['centenas'][unidade_str]

        
    
    # if unidade_str not in digitos['unidades']:
    #     unidade = digitos['dezenas'][dezena_str]
    #     dezena = 1
       
        
    # if centena_str not in digitos['centenas']:
    #     centena = 0
    # if centena_str in digitos['centenas']:
    #     centena = digitos['centenas'][centena_str]
    
    l.append(centena)
    l.append(dezena)
    l.append(unidade)
    return l


get_last_3_numbers(list_string_numbers_raw=list_string_numbers_raw, digitos=digitos)