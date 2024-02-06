class Node:
    def __init__(self,data,Next):
        self.data=data
        self.Next=Next
        
class Linkedlist:
    def __init__(self):
        self.head=None
        
    def insert_at_beginning(self,data):
        node =Node(data,self.head)
        self.head=node
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data, None)
            return
            
        itr=self.head
        while itr.Next:
            itr=itr.Next
        itr.Next=Node(data,None)
    
    def inser_at(self,index,data):
        if index <0 or index >self.length():
            raise Exception("invalid index")
            
        itr=self.head
        count=0
        while itr:
            if count ==index-1:
                node=Node(data,itr.Next)
                itr.Next=node
            itr=itr.Next
            count +=1
            
    def insert_values(self,lst):
        for e in lst :
            self.insert_at_end(e)
        
        
    def insert_after_value(self, data_after, data_to_insert):
        
        itr=self.head
        while itr:
            if itr.data== data_after:
                node=Node(data_to_insert,itr.Next)
                itr.Next=node
            itr=itr.Next
        
    def remove_at(self,index):
        if index <0 or index >self.length():
            raise Exception("invalid index")
        
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                itr.Next=itr.Next.Next
            count +=1
            itr=itr.Next
        
        
    # def remove_by_value(self, data):
    #     itr=self.head
    #     count=0
    #     while itr:
    #         if itr.data==data:
    #             self.remove_at(count)
    #         itr=itr.Next
    #         count +=1
    def remove_by_value(self, data):
        itr=self.head
        
        while itr.Next:
            if itr.Next.data==data:
                itr.Next=itr.Next.Next
            itr=itr.Next
    
    # def remove_value(self,data):
    #     if self.head.data==data:
    #         self.head=self.head.Next
    #         return
        
    #     itr=self.head
    #     while itr:
    #         if itr.Next.data==data:
    #             itr.Next=itr.Next.Next
    #             break
    #         itr=itr.Next
                        
        
    
    def length(self):
        itr=self.head
        count=0
        while itr:
            itr=itr.Next
            count +=1
        return count
    
    def Print(self):
        itr=self.head
        lstr=''
        while itr:
            lstr +=str(itr.data)+'-->'
            itr=itr.Next
        
        print(lstr)
        
    
    
if __name__=='__main__':
    
    ll=Linkedlist()
    ll.insert_at_end(11)
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(6)
    ll.insert_at_beginning(7)
    ll.insert_at_end(10)
    ll.Print()
    ll.inser_at(2, 50)
    ll.Print()
    ll.remove_at(3)
    ll.Print()
    ll.insert_values(["banana","mango","orange"])

    ll.Print()
    print("length",ll.length())
    ll.insert_after_value("mango","apple")
    ll.Print()
    print("length",ll.length())
    ll.remove_by_value("banana")
    ll.Print()
    print("length",ll.length())
