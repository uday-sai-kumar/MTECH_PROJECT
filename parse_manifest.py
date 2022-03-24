

FILE_PATH = "/Users/udaysaikumar/Documents/THESIS/CODES/DATASET/APKTOOl/0a1aa1f3c881c8e8f6ea3a27fb6772c1cb21038e0bc134e702492d84d5d2646f.out/AndroidManifest.xml"

import xml.etree.ElementTree as ET

tree = ET.parse(FILE_PATH)

_root=tree.getroot()

# for _node in _root.findall('uses-permission'):
#     print("___________")
#     _attr = _node.attrib
#     keys = _attr.keys()
#     print(_attr[list(keys)[0]])
# for _node in _root.findall('uses-feature'):
#     print("___________")
#     _attr = _node.attrib
#     keys = _attr.keys()
#     print(_attr[list(keys)[0]])
__root = _root.find('application')

print(__root)
for _node in __root.findall('activity'):
        _attr = _node.attrib
        print(_attr.values())
        print(_attr.keys())

        print('______________________')


#print(a[a.keys()[0]])
