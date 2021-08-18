# using list for queue lead to dynamic array problem of copying and 2*capacity allocation of intial post capacity insertion
# Queue - FIFO

queue = []

queue.insert(0, 10)
queue.insert(0, 20)
queue.insert(0, 30)
queue.insert(0, 40)

print(queue)

queue.pop()
queue.pop()

print(queue)