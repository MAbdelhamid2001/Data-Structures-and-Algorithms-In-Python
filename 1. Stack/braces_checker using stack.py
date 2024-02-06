from collections import deque

def is_matched(op,cl):
    if op =='[' and cl==']':
        return True
    elif op=='{'and cl=='}':
        return True
    elif op=='(' and cl==')':
        return True
    else:
        return False  
def is_balanced(x):
    opened='{[('
    closed=')]}'

    s=deque()
    for i in x:
        if i in opened:
            s.append(i)
    
        if i in closed: 
            if len(s)==0:
                return False
            
            if not is_matched(s.pop(),i):
                return False
    return len(s)==0
    
if __name__=='__main__':

    x="(21)(())"
    if is_balanced(x) == True:
        print('matched')
    else:
        print('Not matched')
        
