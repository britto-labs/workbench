from typing import Dict

from workbench.core.plugin import Plugin


class PluginRegistry:
    """
    Registry for all Workbench plugins.
    """

    def __init__(self):
        self._plugins: Dict[str, Plugin] = {}

    def register(self, plugin: Plugin):
        """Register a plugin."""
        self._plugins[plugin.name] = plugin

    def get(self, name: str):
        """Return a plugin by name."""
        return self._plugins.get(name)

    def all(self):
        """Return all registered plugins."""
        return list(self._plugins.values())