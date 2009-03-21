import httplib, urllib
from xml.dom import minidom
class FamilySearch:
    
    url = "www.dev.usys.org"
    key = "WCQY-7J1Q-GKVV-7DNM-SQ5M-9Q5H-JX3H-CMJK"
    agentname = "legado"
    sessionId = ""
    
    def login(self,username,password):
        uri = "/identity/v1/login"
        
        conn = httplib.HTTPConnection(self.url)
        params = urllib.urlencode({'agent': self.agentname, 'key': self.key, 'username': username,'password': password })
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn.request("POST", uri,params,headers)
        response = conn.getresponse()
        msg =  response.read()
        
        dom = minidom.parseString(msg)
        session =  dom.getElementsByTagName('session')
        self.sessionId = session[0].getAttribute('id')
        if self.sessionId == "":
            return False
        else:
            return True
    
    def getRootInfo(self):
        uri = "/familytree/v1/person/me?sessionId="+self.sessionId
        conn = httplib.HTTPConnection(self.url)
        conn.request("GET",uri)
        r1 = conn.getresponse()
        info =  r1.read()
        conn.close()
        return info