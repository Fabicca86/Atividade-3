import threading
import random
import time
from collections import deque

# Definindo o tamanho do buffer
buffer_size = 10
buffer = deque(maxlen=buffer_size)
buffer_lock = threading.Lock()

# Função do produtor
def producer():
    for _ in range(20):  # Produzindo 20 números
        with buffer_lock:
            if len(buffer) < buffer_size:
                num = random.randint(1, 100)
                buffer.append(num)
                print(f'Produzido: {num}')
        time.sleep(0.1)

# Função do consumidor
def consumer():
    while True:
        with buffer_lock:
            if len(buffer) > 0:
                num = buffer.popleft()
                print(f'Consumido: {num}')
        time.sleep(0.2)

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

start_time = time.time()
producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join(timeout=1)  # Ajuste o timeout conforme necessário

end_time = time.time()

print(f'Tempo de execução: {end_time - start_time:.2f} segundos')
