from bs4 import BeautifulSoup
import sys
import xml.etree.ElementTree as ET
import xmltodict

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} [Favicon URL]")
    sys.exit(0)

#open the file
fileptr = open(sys.argv[1],"r")
 
#read xml content from the file
xml_content= fileptr.read()
 
#change xml format to ordered dict
my_dict=xmltodict.parse(xml_content)

for a in my_dict["fingerprints"]["fingerprint"]:
    print(a)
    print()
