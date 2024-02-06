from collections import deque


class Queue:
    def __init__(self):
        self.buffer=deque()
        
    def enque(self,x):
        self.buffer.appendleft(x)
        
    def deque(self):
        return self.buffer.pop()
        # print(self.buffer.pop())
    
    def size(self):
        return len(self.buffer)
    def is_empty(self):
        return len(self.buffer)==0
    

    
if __name__ =='__main__':
    que=Queue()
    que.enque('1')
    for i in range(15):
        ret=que.deque()
        print(ret)
        que.enque(ret+'0')
        que.enque(ret+'1')
        

    
    
    



    