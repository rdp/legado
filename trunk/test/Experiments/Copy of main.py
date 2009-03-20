

def login(self):
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




import httplib, urllib
conn = httplib.HTTPConnection("www.dev.usys.org")
sessionId="USYS5B2BDAA51DFD2B7F05E49483E627E313.ptap009-034"
params = urllib.urlencode({'agent': "legado", 'sessionId': sessionId})

f = urllib.urlopen("http://www.google.com")
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



conn.close()

