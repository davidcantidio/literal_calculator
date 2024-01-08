import operator

class NumberProcessor:
    def __init__(self):
        self.numDict = {
            'unidades': {
                'zero': 0, 'um': 1, 'dois': 2, 'três': 3, 'quatro': 4,
                'cinco': 5, 'seis': 6, 'sete': 7, 'oito': 8, 'nove': 9,
            },
            'dezenas': {
                'dez': 10, 'vinte': 20, 'trinta': 30, 'quarenta': 40,
                'cinquenta': 50, 'sessenta': 60, 'setenta': 70, 'oitenta': 80,
                'noventa': 90,
            },
            'centenas': {
                'cento': 100, 'duzentos': 200, 'trezentos': 300, 'quatrocentos': 400,
                'quinhentos': 500, 'seiscentos': 600, 'setecentos': 700,
                'oitocentos': 800, 'novecentos': 900,
            }
        }
        self.nonAlgarisms = ['mil', 'milhão', 'milhões']
        self.operators = {
            'mais': operator.add,
            'menos': operator.sub,
            'vezes': operator.mul,
            'dividido por': operator.truediv
        }
        self.teensDict = {
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
        
        
    def process_expression(self, operation):
        operands, operator_word = self.extract_operands_and_operator(operation)

        if None not in operands and operator_word:
            first_operand = self.convert_to_number(operands[0])
            second_operand = self.convert_to_number(operands[1])
            operation_function = self.operators[operator_word]

            return operation_function(first_operand, second_operand)
        else:
            return "Operação inválida"

    
    def extract_operands_and_operator(self, operation):
        for operator_word in self.operators:
            if operator_word in operation:
                operands = operation.split(" {} ".format(operator_word))
                return operands, operator_word
        return [None, None], None
    
    
    def translateTeens (self, algarismo):
        if algarismo in self.teensDict:
            return self.teensDict[algarismo]
        return algarismo
    
    
    def wordList(self, text_operand):
        if text_operand.startswith('mil '):
            text_operand = text_operand.replace('mil', 'um mil')
        clean_string = text_operand.replace('milhões', 'milion').replace('milhão', 'milion').replace('e ', '').strip().lower()
        raw_list = list(map(self.translateTeens, clean_string.split(' ')))
        word_list = [item for sublist in raw_list for item in (sublist if isinstance(sublist, list) else [sublist])]
        return  [i for i in word_list if i not in self.nonAlgarisms]

       
    def figures( self, word_list):
        if 'milion' in word_list:
            return 7 + (word_list.index('milion') -1)
        elif 'mil' in word_list:
            return 4 + (word_list.index('mil') -1)
        return len(word_list)
        

            
    def integerAmount(self, word_list):
        return sum(1 for i in word_list if i not in self.nonAlgarisms)


    def addZeros(self, word_list, number_amount, figures):
        l = [word_list[0]]
        word_list.remove(l[0])
        n_zeros = figures - number_amount
        for i in range(n_zeros):
            l.append('zero')
        l.extend(word_list)
        return l
    
    
    def integerList(self, zero_filled_list):
        l = []
        for number_name in zero_filled_list:
            for magnitude in self.numDict:
                if number_name in self.numDict[magnitude]:
                    l.append(self.numDict[magnitude][number_name])
                    break
        return l
    
    
    def integerNumber(self, integer_list):
        return int(''.join(map(str, integer_list)))

    
    def convertToNumber(self, text_operand):
        word_list = self.wordList(text_operand)
        figures_amount = self.figures(word_list)
        integer_amount = self.integerAmount(word_list)
        zero_filled_list = self.addZeros(word_list, integer_amount, figures_amount)
        integer_list = self.integerList(zero_filled_list)
        return self.integerNumber(integer_list)
        
        # Aqui você pode adicionar métodos para processar e calcular números
