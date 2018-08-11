
import xml.etree.ElementTree as ET
import xmltodict
import requests
from requests.auth import HTTPDigestAuth
from collections import OrderedDict

authentication = HTTPDigestAuth('skupszop.pl', 'b188f14b14c0c5d18209')


#response = requests.get('https://www.elibri.com.pl/api/v1/publishers', auth=authentication)
#response = requests.get('https://www.elibri.com.pl/api/v1/publishers/169/products', auth=authentication)
response = requests.get('https://www.elibri.com.pl/api/v1/products/2a295cf88001f3a1a227', auth=authentication, headers={'X-eLibri-API-ONIX-dialect': '3.0.1'})
xmlData = response.content
dataDict = xmltodict.parse(xmlData)
newDict = OrderedDict()
newDict['a'] = dataDict['ONIXMessage']
newDict['b'] = dataDict['ONIXMessage']

rootXMl = OrderedDict()
rootXMl['root'] = newDict

out = xmltodict.unparse(rootXMl, pretty=True)
print(out.encode('utf-8'))


#text = dataDict['ONIXMessage']['Product']['CollateralDetail']['TextContent']['Text'].encode('utf-8')
#print(text)
#category = dataDict['ONIXMessage']['Product']['DescriptiveDetail']['Subject']['SubjectHeadingText']
#print(category)
