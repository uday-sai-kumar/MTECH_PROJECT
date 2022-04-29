

FILE_PATH = "/Users/udaysaikumar/Documents/THESIS/CODES/DATASET/APKTOOl/AndroidManifest.xml"

import xml.etree.ElementTree as ET

XML_NS = '{http://schemas.android.com/apk/res/android}'
tree = ET.parse(FILE_PATH)

_root = tree.getroot()
#print(_root.attrib)

# for _node in _root.findall('uses-feature'):
#     print("___________")
#     _attr = _node.attrib
#     keys = _attr.keys()
#     print(_attr[list(keys)[0]])
__root = _root.find('application')

_activities = set()
_intent_filters = set()
_uses_permission = set()
_permission = set()
_receivers = set()
_services = set()
_provider = set()
for _node in _root.findall('uses-permission'):
    #print("___________")
    _attr = _node.attrib
    keys = _attr.keys()
    _uses_permission.add(_attr[list(keys)[0]])

__list = ['activity', 'receiver', 'service', 'provider']

for i in range(4):
        for _node in __root.findall(__list[i]):
                __trav = _node.find('intent-filter')
                if __trav is not None:
                        #action and category
                        _a_c = ['action', 'category']
                        for _value in _a_c:
                            for __action in __trav.findall(_value):
                                _attr = __action.attrib
                                keys = _attr.keys()
                                #print('_intent --- > ', _attr)
                                _intent_filters.add(_attr[list(keys)[0]])





                        #data -- > leave it

                        # _intent_filters.append(_attr[])
                _attr = _node.attrib
                #print(_attr)
                keys = _attr.keys()
                #print("over")
                # print(keys)
                # print(_attr.values())
                if i == 0:
                        _activities.add(_attr[XML_NS+'name'])
                elif i == 1:
                        _receivers.add(_attr[XML_NS+'name'])
                elif i == 2:
                        _services.add(_attr[XML_NS + 'name'])
                else:
                        _provider.add(_attr[XML_NS + 'name'])
                # print(_attr[list(keys)[1]])

print(_activities)
print("####################")
print(_intent_filters)
print("####################")
print(_uses_permission)
print("####################")
print(_receivers)
print("####################")
print(_services)
print("#################### provider ")
print(_provider)
#print(a[a.keys()[0]])
