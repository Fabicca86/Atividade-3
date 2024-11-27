import threading
import time

# Texto a ser dividido e analisado
text = ("Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
        "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
        "when an unknown printer took a galley of type and scrambled it to make a type specimen book. "
        "It has survived not only five centuries, but also the leap into electronic typesetting, "
        "remaining essentially unchanged. It was popularized in the 1960s with the release of Letraset sheets "
        "containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker "
        "including versions of Lorem Ipsum.")

# Dividindo o texto em três partes
part1, part2, part3 = text[:len(text)//3], text[len(text)//3:2*len(text)//3], text[2*len(text)//3:]

def char_count(text_part, result, index):
    result[index] = len(text_part)

# Lista para armazenar os resultados
result = [0, 0, 0]

start_time = time.time()

# Criando threads para contar os caracteres
thread1 = threading.Thread(target=char_count, args=(part1, result, 0))
thread2 = threading.Thread(target=char_count, args=(part2, result, 1))
thread3 = threading.Thread(target=char_count, args=(part3, result, 2))

# Iniciando as threads
thread1.start()
thread2.start()
thread3.start()

# Esperando as threads terminarem
thread1.join()
thread2.join()
thread3.join()

# Somando os resultados
total_count = sum(result)

end_time = time.time()

print(f'Total de caracteres: {total_count}')
print(f'Tempo de execução: {end_time - start_time:.4f} segundos')
