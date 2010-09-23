def compareNames(person1,person2):
    if person1.primary_name.first_name == person2.primary_name.first_name:
        return True

def compareTrees(tree1, tree2):
    
    if len(tree1)!= len(tree2):
        print "length is different in the tress"
        return
    
    matched = [False]*len(tree1)
    
    for i in range(len(tree1)):
       if(tree1[i]!= None and tree2[i]!=None):
           if compareNames(tree1[i][0],tree2[i][0]):
               matched[i]=True
       elif (tree1[i]== None and tree2[i]==None):
            matched[i] = True
        
    return matched