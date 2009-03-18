# post an xml file, use DOM to build SOAP message
import sys, httplib
import xml.dom.minidom 

import StringIO

# define namespaces used
ec = "http://schemas.xmlsoap.org/soap/encoding/"
soapEnv = "http://schemas.xmlsoap.org/soap/envelope/"
myns = "http://phonedirlux.homeip.net/types"

# DOM document
domdoc = xml.dom.minidom.Document()

# SOAP envelope namespace
seObj = domdoc.createElementNS(soapEnv, "SOAP-ENV:Envelope")
seObj.setAttributeNS(soapEnv, "SOAP-ENV:encodingStyle", ec)

# add it to the root
domdoc.appendChild(seObj)

header = domdoc.createElement("SOAP-ENV:Header")
seObj.appendChild(header)

body = domdoc.createElement("SOAP-ENV:Body")

readls = domdoc.createElementNS(myns, "ns1:readLS")

string_1 = domdoc.createElement("String_1")
string_1.appendChild(domdoc.createTextNode("Message created with PyXml, your e-mail"))

readls.appendChild(string_1)

body.appendChild(readls)

seObj.appendChild(body)

soapStr = StringIO.StringIO()


# construct the header and post

webservice = httplib.HTTP("www.dev.usys.org/identity/v1/login?key=")
webservice.putrequest("POST", "/rcx-ws/rcx")
webservice.putheader("Host", "www.pascalbotte.be")
webservice.putheader("User-Agent", "My post")
webservice.putheader("Content-type", "text/xml; charset=\"UTF-8\"")
webservice.putheader("Content-length", "%d" % len(soapStr.getvalue()))
webservice.putheader("SOAPAction", "\"\"")
webservice.endheaders()
webservice.send(soapStr.getvalue())

# get the response

statuscode, statusmessage, header = webservice.getreply()
print "Response: ", statuscode, statusmessage
print "headers: ", header
res = webservice.getfile().read()
print res
