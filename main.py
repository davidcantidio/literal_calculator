from number_processor import NumberProcessor

def main():
    # Criar uma instância da classe NumberProcessor
    processor = NumberProcessor()

    # Pedir ao usuário para inserir a expressão matemática
    user_input = input("Digite a expressão matemática (por exemplo, 'dois mais três'): ")

    # Separar a expressão nos operandos e no operador
    operands, operator_word = processor.extract_operands_and_operator(user_input)

    # Verificar se os operandos e o operador são válidos
    if None not in operands and operator_word:
        # Converter os operandos para números
        first_operand = processor.convertToNumber(operands[0])
        second_operand = processor.convertToNumber(operands[1])

        # Realizar a operação matemática
        operation_function = processor.operators[operator_word]
        result = operation_function(first_operand, second_operand)

        print("Resultado:", result)
    else:
        print("Operação inválida")

if __name__ == "__main__":
    main()
