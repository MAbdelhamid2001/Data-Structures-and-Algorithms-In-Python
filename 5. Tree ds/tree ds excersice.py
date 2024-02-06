class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
        
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    
    def get_level(self):
        count=0
        while self.parent !=None:
            count +=1
            self=self.parent
        return count    
    
    def print_tree(self):
        level=self.get_level()
        # end=' '*level+'|'+'_'*level
        end=' '*level*7
        end= end+'|__' if self.parent else ''

        print(end,self.data[1])
        if self.children:
            for child in self.children:
                child.print_tree()
                

def build_product_tree():
    root=TreeNode(('Nilupul','CEO'))
    chinmay=TreeNode(('chinmay','CTO'))
    
    Gels=TreeNode(('HR','Head'))
    Gels.add_child(TreeNode(('Peter','Recruitment Head')))
    Gels.add_child(TreeNode(('Waqas','Policy Manager')))
    
    
    Vishwa=TreeNode(('Vishwa','Infrastructure Head'))
    Vishwa.add_child(TreeNode(('Dhaval','Cloud Manager')))
    Vishwa.add_child(TreeNode(('Abhijit','App Manager')))
    
    chinmay.add_child(Vishwa)
    chinmay.add_child(TreeNode(('Aamir','Application head')))
    
    root.add_child(chinmay)
    root.add_child(Gels)
    
    return root

if __name__=='__main__':
    root=build_product_tree()
    # print(root.get_level())
    root.print_tree()
    
