


def login():
    import httplib, urllib
    conn = httplib.HTTPConnection("www.dev.usys.org")
    key = "WCQY-7J1Q-GKVV-7DNM-SQ5M-9Q5H-JX3H-CMJK"
    username = "api-user-1033"
    password = "104c"
    params = urllib.urlencode({'agent': "legado", 'key': key, 'username': username,'password': password })
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn.request("POST", "/identity/v1/login",params,headers)
    response = conn.getresponse()
    #print response.status, response.reason
    print response.read()
    print response.msg

def identity():
    import httplib, urllib
    conn = httplib.HTTPConnection("www.dev.usys.org")
    sessionId="USYSDAE8276CC3F214379F2058A439ECECB2.ptap009-034"
    
    uri = "/familytree/v1/person/me?sessionId="+sessionId
    print uri
    conn.request("GET",uri)
    r1 = conn.getresponse()
    print r1.status, r1.reason
    print r1.read()
    conn.close()


login()
resp = "<?xml version='1.0' encoding='UTF-8'?><identity xmlns='http://api.familysearch.org/identity/v1' xmlns:fsapi-v1='http://api.familysearch.org/v1 version="1.3.20090210.3423" statusMessage="OK" statusCode="200"><session id="USYSB61BB4B154BCAE70D98E286283DD76E9.ptap009-034" /></identity>"


#if __name__ == "__main__":
#    login()

#params = urllib.urlencode({'agent': "legado", 'sessionId': sessionId})

#f = urllib.urlopen("http://www.google.com")
#print f.read()


#headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
#conn.request("POST", "/familytree/v1/me",params,headers)
#response = conn.getresponse()
##print response.status, response.reason
#print response.read()
##print response.msg



#from elementtree.ElementTree import parse
#
#
#url = 'http://www.dev.usys.org/identity/v1/login?agent=legado&key='+key+'&username='+username+'&password='+password
#WEATHER_NS = 'http://api.familysearch.org/identity/v1'
#
#resp = urllib.urlopen(url).read()
#print resp






#root = parse(resp).getroot()

#conn = httplib.HTTPConnection("www.dev.usys.org")
#conn.request("GET", "/identity/v1/login")
#r1 = conn.getresponse()
#print r1.status, r1.reason


#print root.tag
#
#print root[0].items

#session = rss.findall('session')
#session.get('id')





