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
        end=' '*level*5
        end= end+'|__' if self.parent else ''

        print(end,self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
                
  

def build_product_tree():
    root=TreeNode('Eelectronics')
    
    laptop=TreeNode('laptop')
    laptop.add_child(TreeNode('mac'))
    laptop.add_child(TreeNode('surface'))
    laptop.add_child(TreeNode('thinkpad'))

    cellphone=TreeNode('cellphone')
    cellphone.add_child(TreeNode('iphone'))
    cellphone.add_child(TreeNode('google_pixel'))
    cellphone.add_child(TreeNode('vivo'))
    
    cellphone.children[0].add_child(TreeNode('iphone_XXX'))
    tv=TreeNode('tv')
    tv.add_child(TreeNode('samsung'))
    tv.add_child(TreeNode('LG'))
    
    
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    
    return root

if __name__=='__main__':
    root=build_product_tree()
    # print(root.get_level())
    root.print_tree()

