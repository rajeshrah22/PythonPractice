class QueueError(Exception):  # Choose base class for the new exception.
    pass


class Queue:
    def __init__(self):
        self.__list = []

    def put(self, elem):
        self.__list.insert(0, elem)
    def returnLen(self):
        return len(self.__list)
    def get(self):
        if len(self.__list) > 0:
            val = self.__list[-1]
            del self.__list[-1]
            return val
        else:
            raise QueueError

class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
    def isempty(self):
        if Queue.returnLen(self) == 0:
            return True
        else:
            return False


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
