import os
import warnings
from pathlib import Path

from platformdirs import PlatformDirs


def _env_override(app_name: str, category: str) -> str | None:
    key = app_name.upper().replace("-", "_")
    return os.environ.get(f"{key}_{category.upper()}_HOME")


def _make_dir(path: str, mode: int = 0o700) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    try:
        p.chmod(mode)
    except PermissionError:
        pass
    return p


_CATEGORY_MAP = {
    "config": "user_config_dir",
    "data": "user_data_dir",
    "state": "user_state_dir",
    "cache": "user_cache_dir",
    "log": "user_log_dir",
    "runtime": "user_runtime_dir",
}


class LocalStorage:
    """跨平台应用本地目录管理。

    提供配置、数据、缓存、日志、状态、运行时六个标准目录，
    遵循各平台规范（XDG、macOS、Windows）。

    用法:
        >>> from quanttide import LocalStorage
        >>> store = LocalStorage("my-app")
        >>> isinstance(store.data_dir, Path)
        True

    环境变量覆写（优先级高于默认路径）:
        >>> import os
        >>> os.environ["MY_APP_DATA_HOME"] = "/tmp"
        >>> store = LocalStorage("my-app")
        >>> str(store.data_dir) == "/tmp"
        True
        >>> del os.environ["MY_APP_DATA_HOME"]
    """

    def __init__(self, app_name: str, vendor: str = "quanttide"):
        self._app_name = app_name
        self._vendor = vendor
        self._dirs = PlatformDirs(app_name, vendor)

    def _get_dir(self, category: str) -> Path:
        override = _env_override(self._app_name, category)
        if override:
            return _make_dir(override)
        method = _CATEGORY_MAP[category]
        return _make_dir(getattr(self._dirs, method))

    @property
    def config_dir(self) -> Path:
        return self._get_dir("config")

    @property
    def data_dir(self) -> Path:
        return self._get_dir("data")

    @property
    def state_dir(self) -> Path:
        return self._get_dir("state")

    @property
    def cache_dir(self) -> Path:
        return self._get_dir("cache")

    @property
    def log_dir(self) -> Path:
        return self._get_dir("log")

    @property
    def runtime_dir(self) -> Path:
        try:
            return self._get_dir("runtime")
        except OSError:
            fallback = self.cache_dir / "run"
            warnings.warn(f"RUNTIME_DIR not available, fallback to {fallback}")
            return _make_dir(fallback)
