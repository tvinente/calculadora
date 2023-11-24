def calculadora(numero1, numero2, operacao):

    match operacao:
        case 1:
            return numero1 + numero2
        case 2: 
            return numero1 - numero2
        case 3: 
            return numero1 * numero2
        case 4: 
            return numero1 / numero2

    return 0
    
valor1= float(input ("Digite o primeiro valor: "))
valor2 = float(input ("Digite o segundo valor: "))
operacao = int(input ("Digite o número da operação (1.Somar, 2.Subtrair, 3.Multiplicar ou 4.Dividir): "))
resultado = calculadora(valor1, valor2, operacao)
print("Resultado: %.2f" % resultado)