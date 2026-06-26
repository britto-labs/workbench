from pathlib import Path

import tomllib


CONFIG_FILE = Path("config/workbench.toml")


class ConfigManager:
    def __init__(self):
        with open(CONFIG_FILE, "rb") as file:
            self._config = tomllib.load(file)

    def get(self, section: str):
        return self._config.get(section, {})