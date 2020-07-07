import json
import os.path
import sphobjinv as soi
import sys
import re

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

def haddock_inventory(haddock_dir):
    """Generate a haddock inventory"""

    # This is a terrible hack, but otherwise the user has to pass it in,
    # and I'm not sure where they'd get it from
    index_html_path = os.path.join(haddock_dir, 'index.html')
    with open(index_html_path) as index_html: 
        # This working right relies on maximul much quite a bit!
        match = re.search("<title>(.+)-([0-9.]+).*</title>", index_html.read())
        if not match:
            print("Couldn't get the project and version from the html")
            sys.exit(1)
        project = match.group(1)
        version = match.group(2)

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
    # Args are: project name, haddock dir
    # Perhaps we could infer the project name to be the haddock directory...
    haddock_dir = sys.argv[1]
    print("Generating inventory for haddock dir '{}'".format(haddock_dir))
    haddock_inventory(haddock_dir)
