# Atividade-3
Exercicios para matéria de Sistemas operacionas do UFBRA

Fabiana Carla da Costa Alves - Engenharia da Computação - Linguagem escolhida: python
Atividade 3 – Sistemas Operacionais
Prof. Leandro Azevedo
Atividade prática
Threads

Conceitos de paralelismo de processos – Threads

Crie um programa em uma linguagem de programação de seu domínio para fazer os seguintes exercícios.

## Exercício 1. Produtor-Consumidor 
Objetivo: Implementar um problema clássico de threads, o problema "Produtor-Consumidor", usando um buffer compartilhado.
Descrição:
Crie um buffer (lista ou fila) de tamanho fixo;
Um produtor deve produzir números aleatórios e colocá-los no buffer;
O consumidor deve retirar os números do buffer e consumi-los (imprimir os valores);
Crie um contador de tempo para verificar o tempo de execução dos programas com e sem uso de threads;
Crie um programa que faça essa função sem o uso de threads;
Crie um programa faça o uso de threads para executar o processo Produtor-Consumidor.



## Exercício 2. Contagem de palavras
Objetivo: Contar o número de palavras em um texto usando múltiplas threads.
Descrição:
Crie um contador de tempo para verificar o tempo de execução dos programas com e sem o uso de threads;
Divida o texto abaixo em três partes e crie um método que faça a contagem das palavras em cada parte do texto.
Divida o texto abaixo em três partes e crie um método (thread) para contar as palavras em cada parte do texto.
O programa (processo) deve esperar que as threads terminem antes de imprimir o número total de palavras.

"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularized in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."


## Exercício 3. Calculadora Multithreads
Objetivo: Criar uma calculadora que faça operações matemáticas com múltiplas threads.
Descrição:
Crie um programa que recebe uma lista de operações matemáticas e distribua essas operações entre várias threads para serem realizadas simultaneamente.
Cada thread deve calcular uma operação (soma, subtração, multiplicação, divisão, potenciação e raiz quadrada) e imprimir o resultado.



