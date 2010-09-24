from familysearch_gramps import *
from familysearch_api import *
from familysearch import *

class FSTest():
    
    def test_person_convert(self):
        url = "www.dev.usys.org"
        key = "WCQY-7J1Q-GKVV-7DNM-SQ5M-9Q5H-JX3H-CMJK"
        agentname = "legado"
    
        self.fsapi = FamilySearchAPI(url,key,agentname)
        username = "api-user-1033"
        password = "104c"
        self.fsapi.login(username,password)
        person= self.fsapi.get_user()
        print person
        self.person =  fs_person_to_gramps(person)
        print self.person.primary_name.first_name
        print self.person.get_gender()
        
    
    def find_fstree(self, person, pedigree, index, depth, lst, val=0):
            """Recursively build a list of ancestors"""
    
            if depth > 5 or person == None:
                return

            alive = False
            lst[index] = (person, val, None, alive)
    
            
            mrel = True
            frel = True
            
            parents = pedigree.pedigrees[0].persons[0].parents
            
            if len(parents) > 0:
                for parentid in parents.id:
                    parent = self.FSwebservice.getPersonFromId(parentid)
                    print parent.gender
                    if parent.gender == 1:
                        person.fs_fatherid = parent.fsid
                        person.fs_father = parent
                        father = parent
                        self.find_fstree(father, (2 * index) + 1, depth + 1, lst, frel)
                    elif parent.gender == 0:
                        person.fs_motherid = parent.fsid
                        mother = parent
                        self.find_fstree(mother, (2 * index) + 2, depth + 1, lst, mrel)

    def test_fs_findtree(self):
        fs_famtree = [None]*31
        pedigree = tester.fsapi.get_pedigree()
        print pedigree
        self.find_fstree(self.person,pedigree,0,1,fs_famtree)




if __name__=="__main__":
    tester = FSTest()
    tester.test_person_convert()
    tester.test_fs_findtree()
    