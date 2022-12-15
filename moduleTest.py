#QUEUE DATA TYPE

from queueModules import Queue

fifo = Queue("A", "B", "C")
fifo.dequeue()
fifo.dequeue()


for element in fifo:
    print(element)






