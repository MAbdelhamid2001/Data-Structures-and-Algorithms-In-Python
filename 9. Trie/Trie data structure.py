class TrieNode:
    def __init__(self,char):
        self.char=char
        self.is_end=False
        self.counter=0
        self.children={}
        
class Trie:
    
    def __init__(self):
        self.root=TrieNode("")
        
    def insert(self,word):
        
        curr_node=self.root
        
        for i in word:
            curr_char=i
            if curr_char not in curr_node.children:
                curr_node.children[curr_char]=TrieNode(curr_char) 
                curr_node=curr_node.children[curr_char]
           
    
            else:
                # print(curr_char)
                curr_node=curr_node.children[curr_char]
            
        curr_node.is_end=True
        curr_node.counter +=1   
        
        
    

    def query(self,chars):
        
        self.output=[]
        curr_node=self.root
        
        for ch in chars:
            if ch in curr_node.children:
                curr_node = curr_node.children[ch]
            
            else:
                return []
        
        
        self.dfs(curr_node,chars[:-1])
        #curr_node is o 
        #prefix w
        
        sorted_out=sorted(self.output,key=lambda x:x[1],reverse=True)
        ret=[i[0] for i in sorted_out]
        
        return ret
        
                
        
    def dfs(self,curr_node,prefix):
        
        if curr_node.is_end:
            self.output.append((prefix +curr_node.char,curr_node.counter))
        
        
        for child in curr_node.children.values():
            #curr_node is o 
            #prefix w
            self.dfs(child,prefix+curr_node.char)
            
    

if __name__=='__main__':
    
    trie=Trie()
    trie.insert('won')
    root=trie.root
    # print(root.children['w'].children['o'].children)
    # print(root.children['w'].children['o'].children['n'].is_end)
    # print(root.children['w'].children['o'].is_end)
    # print(root.children['w'].is_end)

    trie.insert('fone')
    trie.insert('fone')
    trie.insert('fone')

    trie.insert('was')
    trie.insert('fork')
    trie.insert('worse')
    trie.insert('what')
    trie.insert('where')
    trie.insert('why')
    trie.insert('why')
    trie.insert('why')
    
    print(root.children['f'].children['o'].children.keys())
    print(root.children['f'].children['o'].children['n'].children['e'].counter)

    
    
    print(trie.query('wh'))


