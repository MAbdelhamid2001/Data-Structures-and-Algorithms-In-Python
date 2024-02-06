class HashTable:
    def __init__(self):
        self.Max=10
        self.arr=[None for i in range(self.Max)]
        
    def get_hash(self,key):
        sum=0
        for i in key :
            sum+=ord(i)
        return sum %self.Max
      
    # def add(self,key,val):
    #     idx=self.get_hash(key)
    #     self.arr[idx]=val
        
    # def get(self,key):
    #     idx=self.get_hash(key)
    #     return self.arr[idx]
    def __setitem__(self,key,val): #python operators
        idx=self.get_hash(key)
        self.arr[idx]=val
        
    def __getitem__(self,key):
        idx=self.get_hash(key)
        return self.arr[idx]
    
    def __delitem__(self,key):
        idx=self.get_hash(key)
        self.arr[idx]=None
    
    

if __name__=='__main__':
    
    
    # t=HashTable()
    # t.add('march 6',130)
    # print(t.get('march 6'))
    
    t=HashTable()
    t['march 6']=130
    t['march 1']=20
    print(t.arr)

    t['march 17']=27
    print(t.arr)
    print(t['march 6'])
    
    # del t['march 6']
    
    # print(t['march 6'])
    #there is  collission happens when some keys have the same index 
    # it results that the last vaule only will be saved 
    #first appraoch for solving this colission
    #is called separatechaining:
    #by putting a list or a linked list on each 
    #place in the table, the complexity will be O(n)
    
    #second approach is called linear probing:
        #if the place was filled with another vaule so 
        #it will search for the next availble free place to store in
        #probing means searching for an empty place
        
    

    
    