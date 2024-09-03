def fibonacci(numero):
    if numero < 0:
        return False

    a, b = 0, 1
    while a < numero:
        a, b = b, a + b

    return a == numero

try:
    numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
    if fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, insira um número válido.")
