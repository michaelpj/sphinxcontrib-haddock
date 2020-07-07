# `sphinxcontrib-haddock`

This repository contains two modules:

## `hs_domain`

This is a Haskell domain for Sphinx. 
At the moment it is a bit limited because we can't distinguish many kinds of Haskell objects from the Haddock info.

So we have:
- Haskell modules
- Haskell "objects": this is just any entity that isn't a module.

## haddock_inventory

This creates an intersphinx inventory file from a built Haddock HTML directory, which *must* be built with quickjump support (since we use the `doc-index.json` which that generates).
The inventory creates items that use the Haskell domain above.

This works for per-package Haddock. 
If you have Haddocks for multiple packages, you will need one inventory per package and then to include them all.
