class HashTable:
    def __init__(self):
        self.Max=10
        self.arr=[[] for i in range(self.Max)]
        
    def get_hash(self,key):
        sum=0
        for i in key :
            sum+=ord(i)
        return sum %self.Max
      
    def __setitem__(self,key,val): #python operators
        idx=self.get_hash(key)
        
        found=False
        for i ,element in enumerate(self.arr[idx]):
            if element[0]==key:
                self.arr[idx][i]=(key,val)
                found=True
                break

        if found ==False:       
            self.arr[idx].append((key,val))
        
        
    def __getitem__(self,key):
        idx=self.get_hash(key)
        
        for i,element in enumerate(self.arr[idx]):
            if element[0]==key:
                return element[1]
    
    def __delitem__(self,key):
        idx=self.get_hash(key)
        for i,element in enumerate(self.arr[idx]):
            if element[0]==key:
                del self.arr[idx][i]
    

if __name__=='__main__':
    
  
    t=HashTable()
    t['march 6']=130
    t['march 1']=20
    print(t.arr)

    t['march 17']=27
    print(t.arr)
    print(t['march 17'])
    
    del t['march 6']
    
    print(t.arr)
    print(t['march 6'])


    
    