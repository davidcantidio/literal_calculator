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
    def Operands(self, operation):
        for element in self.operators:
            return operation.split(" {} ".format(element))
    
    
    def operationOperator (self, operation):
        for o in self.operators:
            if o in operation:
                return operation[o]
    
    
    def translateTeens (self, algarismo):
        if algarismo in self.teensDict:
            return self.teensDict[algarismo]
        return algarismo

    # Aqui você pode adicionar métodos para processar e calcular números
