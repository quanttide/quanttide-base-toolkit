import os
from pathlib import Path

from platformdirs import PlatformDirs


def _env_override(app_name: str, category: str) -> str | None:
    key = app_name.upper().replace("-", "_")
    return os.environ.get(f"{key}_{category.upper()}_HOME")


_CATEGORY_MAP = {
    "config": "user_config_dir",
    "data": "user_data_dir",
    "state": "user_state_dir",
    "cache": "user_cache_dir",
    "log": "user_log_dir",
    "runtime": "user_runtime_dir",
}


class LocalStorage:
    def __init__(self, app_name: str, vendor: str = "quanttide"):
        self._app_name = app_name
        self._vendor = vendor
        self._dirs = PlatformDirs(app_name, vendor)

    @property
    def config_dir(self) -> Path:
        override = _env_override(self._app_name, "config")
        if override:
            return Path(override)
        return Path(self._dirs.user_config_dir)

    @property
    def data_dir(self) -> Path:
        override = _env_override(self._app_name, "data")
        if override:
            return Path(override)
        return Path(self._dirs.user_data_dir)

    @property
    def state_dir(self) -> Path:
        override = _env_override(self._app_name, "state")
        if override:
            return Path(override)
        return Path(self._dirs.user_state_dir)

    @property
    def cache_dir(self) -> Path:
        override = _env_override(self._app_name, "cache")
        if override:
            return Path(override)
        return Path(self._dirs.user_cache_dir)

    @property
    def log_dir(self) -> Path:
        override = _env_override(self._app_name, "log")
        if override:
            return Path(override)
        return Path(self._dirs.user_log_dir)

    @property
    def runtime_dir(self) -> Path:
        override = _env_override(self._app_name, "runtime")
        if override:
            return Path(override)
        return Path(self._dirs.user_runtime_dir)
