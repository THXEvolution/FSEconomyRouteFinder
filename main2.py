import xmltodict
import requests
import json

content = requests.get("https://server.fseconomy.net/data?userkey=641CA2FE49EE6FAE&format=xml&query=aircraft&search=configs").content.decode("utf-8")
parsed = xmltodict.parse(content)
print(json.dumps(parsed, indent=4))
