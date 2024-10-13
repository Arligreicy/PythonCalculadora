def calculadora(numero1, numero2, operacao):
    if operacao == '+':
        return numero1 + numero2
    elif operacao == '-':
        return numero1 - numero2
    elif operacao == '*':
        return numero1 * numero2
    elif operacao == '/':
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Divisão por zero não é permitida."
    else:
        return "Operação Inválida"

# Exemplo de uso:
print(calculadora(10, 5, '+'))