import os
from pathlib import Path

from quanttide import LocalStorage


class TestLocalStorage:
    def test_init(self):
        store = LocalStorage("my-app")
        assert store._app_name == "my-app"
        assert store._vendor == "quanttide"

    def test_config_dir_default(self):
        store = LocalStorage("my-app")
        path = store.config_dir
        assert isinstance(path, Path)
        assert "my-app" in str(path)

    def test_data_dir_default(self):
        store = LocalStorage("my-app")
        path = store.data_dir
        assert isinstance(path, Path)
        assert "my-app" in str(path)

    def test_cache_dir_default(self):
        store = LocalStorage("my-app")
        path = store.cache_dir
        assert isinstance(path, Path)
        assert "my-app" in str(path)

    def test_log_dir_default(self):
        store = LocalStorage("my-app")
        path = store.log_dir
        assert isinstance(path, Path)
        assert "my-app" in str(path)

    def test_state_dir_default(self):
        store = LocalStorage("my-app")
        path = store.state_dir
        assert isinstance(path, Path)
        assert "my-app" in str(path)

    def test_runtime_dir_default(self):
        store = LocalStorage("my-app")
        path = store.runtime_dir
        assert isinstance(path, Path)
        assert "my-app" in str(path)

    def test_env_override(self):
        os.environ["MY_APP_DATA_HOME"] = "/tmp/custom-data"
        store = LocalStorage("my-app")
        assert store.data_dir == Path("/tmp/custom-data")
        del os.environ["MY_APP_DATA_HOME"]

    def test_env_override_config(self):
        os.environ["MY_APP_CONFIG_HOME"] = "/tmp/custom-config"
        store = LocalStorage("my-app")
        assert store.config_dir == Path("/tmp/custom-config")
        del os.environ["MY_APP_CONFIG_HOME"]

    def test_custom_vendor(self):
        store = LocalStorage("my-app", vendor="custom")
        assert store._vendor == "custom"

    def test_path_contains_app_name(self):
        store = LocalStorage("test-app")
        assert "test-app" in str(store.data_dir)
