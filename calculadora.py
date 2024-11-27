import threading
import math

# Funções para as operações matemáticas
def add(x, y):
    print(f'{x} + {y} = {x + y}')

def subtract(x, y):
    print(f'{x} - {y} = {x - y}')

def multiply(x, y):
    print(f'{x} * {y} = {x * y}')

def divide(x, y):
    if y != 0:
        print(f'{x} / {y} = {x / y}')
    else:
        print('Divisão por zero não é permitida')

def power(x, y):
    print(f'{x} ^ {y} = {x ** y}')

def sqrt(x):
    if x >= 0:
        print(f'√{x} = {math.sqrt(x)}')
    else:
        print('Raiz quadrada de número negativo não é permitida')

# Função para solicitar valores do usuário
def get_values():
    x = float(input('Digite o primeiro valor: '))
    y = float(input('Digite o segundo valor: '))
    return x, y

# Função para distribuir e executar as operações
def execute_operation(operation, x, y):
    if operation == 'add':
        add(x, y)
    elif operation == 'subtract':
        subtract(x, y)
    elif operation == 'multiply':
        multiply(x, y)
    elif operation == 'divide':
        divide(x, y)
    elif operation == 'power':
        power(x, y)
    elif operation == 'sqrt':
        sqrt(x)
        sqrt(y)

# Lista de operações a serem realizadas
operations = ['add', 'subtract', 'multiply', 'divide', 'power', 'sqrt']

# Solicitando valores do usuário
x, y = get_values()

# Criando e iniciando threads para cada operação
threads = []
for operation in operations:
    thread = threading.Thread(target=execute_operation, args=(operation, x, y))
    threads.append(thread)
    thread.start()

# Esperando que todas as threads terminem
for thread in threads:
    thread.join()
