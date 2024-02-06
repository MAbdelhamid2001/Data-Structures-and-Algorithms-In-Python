class BinarySearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        


    def add_child(self,data):
        if data == self.data:
            return
        
        elif data<self.data:
            if self.left :
                self.left.add_child(data)
                
            else: 
                self.left=BinarySearchTreeNode(data)

            
            
        else:
            if self.right :
                self.right.add_child(data)
                
            else: 
                self.right=BinarySearchTreeNode(data)            

    def in_order_traversal(self):
        elements=[]
        
        #visit left tree
        if self.left:
            elements+=self.left.in_order_traversal()
        
        #visit base node
        elements.append(self.data)
        
        #visit right tree
        if self.right:
            elements+=self.right.in_order_traversal()
        
        return elements
    
        
    def pre_order(self):
        els=[]
        
        els.append(self.data)
        
        if self.left:
            els +=self.left.pre_order()
            
        if self.right:
            els +=self.right.pre_order()
                    
        return els
    
    def post_order(self):
        els=[]
        
        els.append(self.data)
        
        if self.left:
            els +=self.left.pre_order()
            
        if self.right:
            els +=self.right.pre_order()
        
        els.append(self.data)

                    
        return els
        
    def search(self,data):
        if data==self.data:
            return True
        elif data <self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        elif data>self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False
                
        
                   
    def find_min(self):
        
        if self.left:
            return self.left.find_min()
        else:
            return self.data
            
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else: return self.data
        
    def calculate_sum(self):
        
        if self.left:
            left_sum =self.left.calculate_sum()
        else:
            left_sum= 0
        
        if self.right:
            right_sum =self.right.calculate_sum() 
        else:
            right_sum= 0
        
        return self.data+ left_sum+right_sum
         
    
    # breadth first search #lever order traversing
    def level_order(self):#breadth first search  
        h=self.get_height()
        els=[]
        for i in range(1,h+1):
            els +=self.print_level_nodes(i)
        
        return els
            
        
        
    def print_level_nodes(self,level):

        els=[]
        if level == 1:
            # print(self.data,end=" ")
            # curr=self.data
            els.append(self.data)
        elif level>1:
            if self.left:
                els +=self.left.print_level_nodes(level-1)
                 
            if self.right:
                els +=self.right.print_level_nodes(level-1)  
                
        return els            
            
    
    
        
    
    def get_height(self):
        
        if self.left:
            lheight =self.left.get_height()
        else:
            lheight= 0
        
        if self.right:
            rheight =self.right.get_height()
        else:
            rheight =0
        
        if lheight>rheight: # comparing to get max +1
            return lheight+1
        else:
            return rheight+1
    
    
            
        
    def delete(self,val):
        
        #imagine ur searching for the item to delete
        if val <self.data:
            if self.left:
                self.left=self.left.delete(val)
            
        elif val>self.data:
            if self.right:
                self.right=self.right.delete(val)
            
        else:
            
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
                
            elif self.right is None:
                return self.left
            
                
            minn=self.right.find_min()
            self.data=minn
            self.right=self.right.delete(minn)
            
        
        return self
        
    def is_balanced(self):
        if self.left:
           self.left.is_balanced()
           l_h=self.left.get_height()
        else:
            l_h=0
        if self.right:
            self.right.is_balanced()
            r_h=self.right.get_height()
        else:
            r_h=0
        
        df=abs(l_h-r_h)
        if df <=1:
            return 'Balanced'
        else:
            return 'Not Balanced'
    
    
            
    def is_bst(self):     
        
        vals=root.in_order_traversal()
    
        Is_bst=1
        for i in range(0,len(vals)-1):
            # print(i)
            if vals[i]<vals[i+1]:
                continue
            else:
                Is_bst=0
                break
        
        if Is_bst:
            return 'BST' 
        else:
            return 'Not BST'
            
                
        
            
def build_tree(elements):
    root=BinarySearchTreeNode(elements[0])
    
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root



if __name__ =='__main__':


    # nums=[17,4,1,20,9,23,18,34]# balanced
    # nums=[15,12,7,14,27,20,23,88 ]
    nums=[17,4,1,20,9,8]# not balanced

    # root=build_tree(nums)
    
    # print(root.inorder())
    
    # print(root.search(34))
    # print(root.find_min())
    # print(root.find_max())
    
    # print(root.calculate_sum())
    #  # print(root.post_order())
    # print(root.level_order())
    root = BinarySearchTreeNode(9)
    root.left = BinarySearchTreeNode(1)  
    root.right = BinarySearchTreeNode(10)  
    root.left.left = BinarySearchTreeNode(0)
    root.left.right = BinarySearchTreeNode(3)
    root.left.right.right = BinarySearchTreeNode(2)  
    
    print(root.is_bst())


        
    

        
        
        
        
        
        
        
        

