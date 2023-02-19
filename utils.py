from io import StringIO
import xml.etree.ElementTree as ET

def parseXML(xml):
    it = ET.iterparse(StringIO(xml))
    for _, el in it:
        _, _, el.tag = el.tag.rpartition('}')

    root = it.root

    return root