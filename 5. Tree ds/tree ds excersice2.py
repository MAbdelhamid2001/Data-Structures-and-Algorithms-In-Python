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
    
    def print_tree(self,l):
        level=self.get_level()
        if level<=l:
            # end=' '*level+'|'+'_'*level
            end=' '*level*5
            end= end+'|__' if self.parent else ''
            print(end,self.data)
        if self.children:
            for child in self.children:
                child.print_tree(l)
                
  

def build_product_tree():
    root=TreeNode('Global')
    
    India=TreeNode('India')
    
    
    Gujarat=TreeNode('Gujarat')
    Gujarat.add_child(TreeNode('Ahmedabad'))
    Gujarat.add_child(TreeNode('Baroda'))

    karnatka=TreeNode('karnatka')
    karnatka.add_child(TreeNode('Bangluru'))
    karnatka.add_child(TreeNode('Mysore'))
    
    India.add_child(Gujarat)
    India.add_child(karnatka)

    ###
    USA=TreeNode('USA')
    
    Newjersey=TreeNode('Newjersey')
    Newjersey.add_child(TreeNode('princeton'))
    Newjersey.add_child(TreeNode('trenton'))

    california=TreeNode('california')
    california.add_child(TreeNode('san francisco'))
    california.add_child(TreeNode('Mpuntain view'))
    california.add_child(TreeNode('Palo Alto'))

    USA.add_child(Newjersey)
    USA.add_child(california)

    root.add_child(India)
    root.add_child(USA)
    
    return root

if __name__=='__main__':
    root=build_product_tree()
    # print(root.get_level())
    root.print_tree(3)

