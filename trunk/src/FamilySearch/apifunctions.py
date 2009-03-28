import httplib, urllib
from xml.dom import minidom
from elementtree.ElementTree import XML
from gen.lib.person import Person
from gen.lib.name import Name

class FamilySearch:
    
    url = "www.dev.usys.org"
    key = "WCQY-7J1Q-GKVV-7DNM-SQ5M-9Q5H-JX3H-CMJK"
    agentname = "legado"
    sessionId = ""
    FS_NS = 'http://api.familysearch.org/familytree/v1'
    conn =None
    def login(self,username,password):
        uri = "/identity/v1/login"
        
        self.conn = httplib.HTTPConnection(self.url)
        params = urllib.urlencode({'agent': self.agentname, 'key': self.key, 'username': username,'password': password })
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        self.conn.request("POST", uri,params,headers)
        response = self.conn.getresponse()
        msg =  response.read()
#        print msg
        try:
            dom = minidom.parseString(msg)
            session =  dom.getElementsByTagName('session')
            self.sessionId = session[0].getAttribute('id')
        except:
            print "error parsing login message"
            print msg
            pass
        
        if self.sessionId == "":
            return False
        else:
            return True
    
    def getRoot(self):
        uri = "/familytree/v1/person/me?sessionId="+self.sessionId
        conn = httplib.HTTPConnection(self.url)
        conn.request("GET",uri)
        r1 = conn.getresponse()
        xmltext =  r1.read()
        person = self.parsePerson(xmltext)
        return person
    
    def getPersonFromId(self, id):
        uri = "/familytree/v1/person/%s?sessionId="%id+self.sessionId
        conn = httplib.HTTPConnection(self.url)
        conn.request("GET",uri)
        r1 = conn.getresponse()
        xmltext =  r1.read()
        person = self.parsePerson(xmltext)
        return person

    def parsePerson(self,xmltext):
       
        root =  XML(xmltext)
        person = Person()
        person.fsid = root.find("{%s}persons/{%s}person/{%s}information/{%s}alternateIds/{%s}id"%(self.FS_NS,self.FS_NS,self.FS_NS,self.FS_NS,self.FS_NS)).text
        person.gender = self.getSex(root.find("{%s}persons/{%s}person/{%s}information/{%s}gender"%(self.FS_NS,self.FS_NS,self.FS_NS,self.FS_NS)).text)
        person.living = root.find("{%s}persons/{%s}person/{%s}information/{%s}living"%(self.FS_NS,self.FS_NS,self.FS_NS,self.FS_NS)).text
        
        name = Name()
        names = root.find("{%s}persons/{%s}person/{%s}assertions/{%s}name"%(self.FS_NS,self.FS_NS,self.FS_NS,self.FS_NS))
        
        for element in names.findall("{%s}forms/{%s}form/{%s}pieces/{%s}piece"%(self.FS_NS,self.FS_NS,self.FS_NS,self.FS_NS)):
            type = element.get('type')
            value = element.find("{%s}value"%self.FS_NS).text
            if type == "Given":
                if name.first_name == "":
                    name.set_first_name(value)
                else:
                    name.set_first_name(name.first_name +" "+value) 
            if type == "Family":
                name.set_surname(value)
        
        person.primary_name= name
        
        parents_tree =   root.findall("{%s}persons/{%s}person/{%s}assertions/{%s}relationship/{%s}parent"%(self.FS_NS,self.FS_NS,self.FS_NS,self.FS_NS,self.FS_NS))
         
        for parent_tree in parents_tree:
#            refid =  parent_tree.get("ref")
#            print refid
#            parent = self.getPersonFromId(refid)
#            print parent.gender
#            if parent.gender == 1:
#                person.fs_fatherid = parent.fsid
#                person.fs_father = parent
#            elif parent.gender == 0:
#                person.fs_motherid = parent.fsid
#                person.mother = parent
            refid =  parent_tree.get("ref")
            person.parents_ids.append(refid)
        
        return  person
    
    def getSex(self,str):
        if str == "Male":
            return 1
        if str == "Female":
            return 0
        else:
            return 2
