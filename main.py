from io import StringIO
import xml.etree.ElementTree as ET
import requests
import utils
from datasource import Datasource

# Show available Planes and choose one
content = requests.get("https://server.fseconomy.net/data?userkey=641CA2FE49EE6FAE&format=xml&query=aircraft&search=configs").content
planes = utils.parseXML(content.decode("utf-8"))

for i, child in enumerate(planes):
    print(f"[{i}] {child[0].text}")

planeNum = int(input("Choose Aircraft: "))

# Get registrations of plane type
content = requests.get(f"https://server.fseconomy.net/data?userkey=641CA2FE49EE6FAE&format=xml&query=aircraft&search=makemodel&makemodel={planes[planeNum][0].text}").content
registrations = utils.parseXML(content.decode("utf-8"))

depth = int(input("Choose search depth: "))

datasource = Datasource(registrations, depth)
