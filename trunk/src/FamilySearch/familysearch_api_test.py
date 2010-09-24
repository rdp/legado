
from gen.lib.person import Person
import familysearch_gramps

def get_parent(pedigree,index):
    parent = Person()
    parent.fsid = pedigree.pedigrees[0].persons[index].parents[0].parents[0].id
    fs_gender = pedigree.pedigrees[0].persons[index].parents[0].parents[0].gender
    parent.gender= familysearch_gramps.convert_sex(fs_gender)
    print parent.fsid," ",parent.gender
    return parent

def build_fstree(fsapi,tree):
    
    alive = False
    
    pedigree = fsapi.get_pedigree(ancestors=4)
    print pedigree
#    lst[index] = (person,val,None,alive)

    
    for index, person in enumerate(pedigree.pedigrees[0].persons):
        name =  person.assertions.names[0].value.forms[0].fullText
        fs_gender = person.assertions.genders[0].value.type
        print index,name,fs_gender
        gramp_person = Person(None,name)
#        gramp_person.set_primary_name(name)
        gender = familysearch_gramps.convert_sex(fs_gender)
        gramp_person.set_gender(gender)
        tree[index]= (gramp_person,True,None,alive)
        
        
    return tree
#    for parent in pedigree.pedigrees[0].persons[0].parents[0].parents:
#        print parent.gender

#    for person in pedigree.pedigrees[0].persons:
#        print person.assertions.genders[0].value.type
    
if __name__=="__main__":
    
    per = Person(None,"hello")
    print per
    
    url = "www.dev.usys.org"
    key = "WCQY-7J1Q-GKVV-7DNM-SQ5M-9Q5H-JX3H-CMJK"
    agentname = "legado"

    from familysearch_api import FamilySearchAPI
    
    fsapi = FamilySearchAPI(url,key,agentname)
    username = "api-user-1033"
    password = "104c"
    fsapi.login(username,password)
    current_user = fsapi.get_user()
#    print current_user
#    pedigree = fsapi.get_pedigree(ancestors=4)
#    print pedigree
#    build_tree(pedigree,list())
    
#    print pedigree.pedigrees[0].persons[0].parents
    fs_famtree = [None]*31
    tree = build_fstree(fsapi, fs_famtree)
    print tree
#    print pedigree.pedigrees[0].persons[0].parents[0].parents

#    print get_parents(pedigree, 0)