
def isEmpty(queue):
    if not queue:
        return True
    else:
        return False
    
def getHead(queue):
    return queue[0]

def enQueue(q,x):
    q.append(x)

def deQueue(queue):
    queue.pop(0)

queue = [1,2,3,4]


deQueue(queue)
deQueue(queue)
deQueue(queue)
enQueue(queue,5)
enQueue(queue,6)
#enQueue(queue,7)

print(queue)
