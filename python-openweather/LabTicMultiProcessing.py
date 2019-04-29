import time
from multiprocessing import Process

def cuad(n):
    return n*n


tiempo1 = time.time()
a = [cuad(i) for i in range(1,1000)]
tiempo2 = time.time()

print('Tiempo de ejecución sin multiproceso: '+ str(tiempo2-tiempo1))

tiempo1 = time.time()
a = [i for i in range(1,1000)]
processes = []
for i in a:
    process = Process(target=cuad, args=(i,))
    processes.append(process)

    process.start()
tiempo2 = time.time()
print('Tiempo de ejecución con multiproceso: '+ str(tiempo2-tiempo1))