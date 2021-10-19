
# Import all the modules from this directory
from spydrnet.ir.definition import Definition


# Following section will extend all the classes imported in this file

from spydrnet import get_active_plugins
import importlib
for name, plugin in get_active_plugins().items():
    ext = importlib.import_module("%s.ir" % name)
    ImportedModules = [attribute for attribute in dir(ext) if \
            callable(getattr(ext, attribute)) and \
                attribute.startswith('__') is False]

    for eachModule in ImportedModules:
        if eachModule in globals():
            pluginModule = ext.__dict__[eachModule]
            baseModule = globals()[eachModule]
            print(f"Extending {baseModule} with {pluginModule}")
            locals()[eachModule] = type(eachModule, (baseModule, object), pluginModule.__dict__.copy())
