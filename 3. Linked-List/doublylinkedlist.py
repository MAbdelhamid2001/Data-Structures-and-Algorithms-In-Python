class Node:
    def __init__(self,prev=None,data=None,Next=None):
        self.data=data
        self.Next=Next
        self.prev=prev

class Linkedlist:
    def __init__(self):
        self.head=None
        
    def insert_at_beginning(self,data):
        if self.head is None:           
            self.head=Node(None,data,self.head)
            
        else:
                
            node=Node(None,data,self.head)
            self.head.prev=node
            self.head=node
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(None,data, None)
            return
        else:
            itr=self.head
            while itr.Next:
                itr=itr.Next
            itr.Next=Node(itr,data,None)
            
    
    def inser_at(self,index,data):
        if index <0 or index >self.length():
            raise Exception("invalid index")
            
        itr=self.head
        count=0
        while itr:
            if count ==index-1:
                node=Node(itr,data,itr.Next)
                if node.next:
                    node.Next.prev=node
                itr.Next=node
            itr=itr.Next
            count +=1
            
            
    def insert_values(self,lst):
        for e in lst :
            self.insert_at_end(e)
        
        
        
        
    def remove_at(self,index):
        if index <0 or index >self.length():
            raise Exception("invalid index")
        
        if index ==0:
            itr=self.head
            self.head=itr.Next
            self.head.prev=None
            
            return
            
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                itr.Next=itr.Next.Next
                itr.Next.prev=itr
            count +=1
            itr=itr.Next
        
        
        
        
    def get_last_node(self):
        itr=self.head
        while itr.Next:
            itr=itr.Next
        return itr
    
    def length(self):
        itr=self.head
        count=0
        while itr:
            itr=itr.Next
            count +=1
        return count
    
    def Print_forward(self):
        itr=self.head
        print("head",self.head.data)
        lstr=''
        while itr:
            lstr +=str(itr.data)+'-->'
            itr=itr.Next
        
        print(lstr)
        
    def Print_backward(self):
        itr=self.get_last_node()
        print("head",self.head.data)
        lstr=''
        while itr:
            lstr +=str(itr.data)+'-->'
            itr=itr.prev
        
        print(lstr)
        
        
    
    
if __name__=='__main__':
    
    ll=Linkedlist()
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(6)
    # ll.insert_at_beginning(7)
    ll.insert_at_end(10)
    ll.insert_at_end(11)
    ll.insert_at_end(12)
    ll.insert_at_end(13)
    
    ll.Print_forward()
    ll.remove_at(2)
    ll.Print_forward()
    ll.Print_backward()
    # ll.Print_rev()
