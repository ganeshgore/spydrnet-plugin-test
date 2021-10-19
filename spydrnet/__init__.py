"""
SpyDrNet
========

SpyDrNet is an EDA tool for analyzing and transforming netlists.

See https://byuccl.github.io/spydrnet for more details.
"""

# Release data
# from spydrnet import release


import importlib
import pkgutil
import pathlib
import sys
import os
sys.path.append(os.getcwd())

discovered_plugins = {
    name: importlib.import_module(name)
    for finder, name, ispkg
    in pkgutil.iter_modules()
    if name.startswith('spydrnet_')
}
print("Installed Plugins", discovered_plugins.keys())


def get_active_plugins():
    active_plugins = {}
    config_file = os.path.join(pathlib.Path.home(), ".spydrnet")
    if os.path.isfile(config_file):
        for plugin in open(config_file, "r").read().split():
            if active_plugins.get(plugin, None):
                print("Plugin %s is not installed " % plugin)
                continue
            active_plugins.update({plugin: discovered_plugins[plugin]})
    else:
        with open(config_file, "w") as fp:
            fp.write("\n".join(discovered_plugins.keys()))
        active_plugins = discovered_plugins
    return active_plugins


print("Active Plugins", get_active_plugins().keys())
