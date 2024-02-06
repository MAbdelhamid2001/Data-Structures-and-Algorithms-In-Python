class HashTable:
    def __init__(self):
        self.Max=10
        self.arr=[None for i in range(self.Max)]
        
    def get_hash(self,key):
        sum=0
        for i in key :
            sum+=ord(i)
        return sum %self.Max
      
    def __setitem__(self,key,val): #python operators
        idx=self.get_hash(key)
        
        if self.arr[idx] == None:
            self.arr[idx]=(key,val)
            
        else:
             new_idx=self.get_new_index(key,idx)
             self.arr[new_idx]=(key,val)
    
    def get_new_index(self,key,idx):
        indecies=[*range(idx,len(self.arr))]+[*range(0,idx)]
        for i in indecies:
            if self.arr[i]==None:
                return i
            if self.arr[i][0]==key:
                return i
        raise Exception('HashMap is Full')
        
        
    def __getitem__(self,key):
        idx=self.get_hash(key)
        if self.arr[idx]==None:
            return
        
        indecies=[*range(idx,len(self.arr))]+[*range(0,idx)]
        for i in indecies:
            if self.arr[i][0]==key:
                return self.arr[i][1]
    
    def __delitem__(self,key):
        idx=self.get_hash(key)
        indecies=[*range(idx,len(self.arr))]+[*range(0,idx)]
        for i in indecies:
            if self.arr[i]== None:
                return
            
            if self.arr[i][0]==key:
                 self.arr[i]=None

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
    t["nov 1"] = 1
    t["march 33"] = 234
    t["april 1"]=87
    t["april 2"]=123
    t["april 3"]=234234
    t["april 4"]=91
    t["May 22"]=4
    print(t.arr)
    t["May 7"]=47
    t["Jan 1"]=0