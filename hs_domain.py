from sphinxcontrib.domaintools import *

def hs_domain():
    return custom_domain('HaskellDomain',
        name  = 'hs',
        label = "Haskell",

        elements = dict(
            hstype = dict(
                objname = "Haskell Type",
            ),
            hsfun = dict(
                objname = "Haskell Function",
            ),
            hsmod = dict(
                objname = "Haskell module",
            ),
        )
    )

def setup(app):
    app.add_domain(hs_domain())
