import json
import os.path
import sphobjinv as soi
import sys

def objects_from_index(index_json):

    modules = set()
    entries = []
    for item in indexJson:
        entry = soi.DataObjStr(name=item['name'], domain='hs', role='whatever', priority='1', uri=item['link'], dispname='-')
        entries.append(entry)
        modules.add(item['module'])
    for mod in modules:
        entry = soi.DataObjStr(name=mod, domain='hs', role='module', priority='1', uri="{}.html".format(mod), dispname='-')
        entries.append(entry)

    return entries

def inventory_from_index(project, version, index_json):
    inv = soi.Inventory()
    inv.project = project
    inv.version = version
    inv.objects.extend(haddock_objects(index_json))
    return inv

def haddock_inventory(project, version, haddock_dir):
    with open(os.path.join(haddock_dir, 'doc-index.json')) as doc_index:
        index_json = json.load(doc_index)

    inv = inventory_from_index(project, version, index_json)
    text = inv.data_file(contract=True)
    ztext = soi.compress(text)
    soi.writebytes(os.path.join(haddock_dir, 'objects.inv'), ztext)

if __name__ == "__main__":
    haddock_inventory(sys.argv[1:])
