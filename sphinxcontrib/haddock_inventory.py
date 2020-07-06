import json
import os.path
import sphobjinv as soi
import sys

def objects_from_index(index_json):

    modules = set()
    entries = []
    for item in index_json:
        for name in item['name'].split(' '):
            module = item['module']
            entry = soi.DataObjStr(name="{}.{}".format(module, name), domain='hs', role='hsobj', priority='1', uri=item['link'], dispname=name)
            entries.append(entry)
            modules.add(module)
    for mod in modules:
        entry = soi.DataObjStr(name=mod, domain='hs', role='hsmod', priority='1', uri="{}.html".format(mod.replace('.','-')), dispname='-')
        entries.append(entry)

    return entries

def inventory_from_index(project, version, index_json):
    inv = soi.Inventory()
    inv.project = project
    inv.version = version
    inv.objects.extend(objects_from_index(index_json))
    return inv

def haddock_inventory(project, version, haddock_dir):
    index_path = os.path.join(haddock_dir, 'doc-index.json')
    if not os.path.exists(index_path):
        print("'doc-index.json' not present in Haddock dir")
        sys.exit(1)
    with open(index_path) as doc_index:
        index_json = json.load(doc_index)

    inv = inventory_from_index(project, version, index_json)
    text = inv.data_file(contract=True)
    ztext = soi.compress(text)
    soi.writebytes(os.path.join(haddock_dir, 'objects.inv'), ztext)

def main():
    haddock_inventory("", "", sys.argv[1])
