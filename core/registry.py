import importlib.util
from typing import Dict, List, Tuple

class PluginRegistry:
    def __init__(self):
        self.plugins: Dict[str, Tuple] = {}

    def register(self, name: str, plugin_class:
        type):
        self.plugins[name] = plugin_class

    def get_plugins(self) -> Dict[str, Tuple]:
        return self.plugins
