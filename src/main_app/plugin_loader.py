from inspect import isclass
from pkgutil import iter_modules
from pathlib import Path
from importlib import import_module
from typing import List
from main_app.base import BasePlugin
from main_app.plugin_response import PluginResponse


class PluginLoader:

    _loaded = {}
    _initialized = {}

    def load_plugins(self, plugin_package):
        # iterate through the modules in the current package
        package_dir = Path(plugin_package.__file__).resolve().parent
        for (_, module_name, _) in iter_modules([package_dir]):

            # import the module and iterate through its attributes
            module = import_module(module_name, package_dir)
            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)

                # Only import classes which are subclasses from our plugin base
                if isclass(attribute) and issubclass(attribute, BasePlugin) and BasePlugin.__name__ != attribute.__name__:
                    # Add the class to this package's variables
                    globals()[attribute_name] = attribute
                    self._loaded[attribute_name] = attribute

    def describe_plugins(self) -> List[str]:
        return [f"{name} v{cl.version} - {cl.description} File:{cl.__module__}" for name, cl in self._loaded.items()]

    def initialize_loaded_plugins(self):
        self._initialized = {k: v() for (k, v) in self._loaded.items()}

    def execute_loaded_plugins(self, standard_frames) -> List[PluginResponse]:
        responses = []
        for p in self._initialized.values():
            responses.extend(p.do_work(standard_frames))
        return responses

