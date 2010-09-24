import httplib
import urllib
from familysearch import *

class FamilySearchAPI:

    def __init__(self,url,developer_key,agent_name):
        self.url = url
        self.developer_key = developer_key
        self.agent_name = agent_name
        
    def get_endpoint(self,endpoint):
        conn = httplib.HTTPConnection(self.url)
        conn.request("GET",endpoint)
        r = conn.getresponse()
        json_output =  r.read()
        return json_output
        
    def login(self,username,password):
        uri = "/identity/v2/login"
        self.conn = httplib.HTTPConnection(self.url)
        params = urllib.urlencode({'dataFormat':'application/json','agent': self.agent_name, 'key': self.developer_key, 'username': username,'password': password })
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        self.conn.request("POST", uri,params,headers)
        response = self.conn.getresponse()
        msg =  response.read()
#        print msg
        try:
            json_dict = json.loads(msg)
            self.session_id =  json_dict["session"]['id']
            
        except:
            print "error login the API"
            print msg
            pass
        
        if self.session_id == "":
            return False
        else:
            return True

    def get_user(self):
        endpoint = "/familytree/v2/person?dataFormat=application/json&sessionId="+self.session_id
        json_output = self.get_endpoint(endpoint)
        self.user = parse_current_user(json_output)
        return self.user
    
    def get_pedigree(self,id=None,ancestors=1): #returns by default the user's pedigree
        if id is None:
            id = self.user.id
        endpoint = "/familytree/v2/pedigree/%s?dataFormat=application/json&sessionId=%s&ancestors=%s"%(id,self.session_id,ancestors)
        json_output = self.get_endpoint(endpoint)
        pedigree = parse_familytree(json_output)
        return pedigree


def load_json(input):
    if hasattr(input, "read"):
        data = json.load(input)
    else:
        data = json.loads(input)
    
    return data

def parse_familytree(input):
    """Parse specified file or string and return a FamilyTree object created from it"""
    data = load_json(input)
    return FamilyTree.from_json(data)


def parse_current_user(input):
    """Parse specified file or string and return a Person object created from it"""
    data = load_json(input)
    if len(data["persons"])>1:
        #TODO catch this exception
        print "user has multiple identities ?"
        exit(0)
    current_user = Person.from_json(data["persons"][0])
    return current_user