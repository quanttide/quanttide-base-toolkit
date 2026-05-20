import warnings
from pathlib import Path
from unittest.mock import PropertyMock, patch

import pytest

from quanttide import LocalStorage
from quanttide.storage import _make_dir


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

    def test_env_override(self, monkeypatch):
        monkeypatch.setenv("MY_APP_DATA_HOME", "/tmp/custom-data")
        store = LocalStorage("my-app")
        assert store.data_dir == Path("/tmp/custom-data")

    def test_env_override_config(self, monkeypatch):
        monkeypatch.setenv("MY_APP_CONFIG_HOME", "/tmp/custom-config")
        store = LocalStorage("my-app")
        assert store.config_dir == Path("/tmp/custom-config")

    def test_custom_vendor(self):
        store = LocalStorage("my-app", vendor="custom")
        assert store._vendor == "custom"

    def test_path_contains_app_name(self):
        store = LocalStorage("test-app")
        assert "test-app" in str(store.data_dir)

    def test_make_dir_permission_error_ignored(self):
        with patch("pathlib.Path.chmod", side_effect=PermissionError):
            path = _make_dir("/tmp/quanttide-test-perm")
            assert path.exists()

    def test_runtime_dir_fallback_on_oserror(self):
        store = LocalStorage("my-app")
        cache_dir = store.cache_dir
        with patch.object(
            type(store._dirs), "user_runtime_dir", new_callable=PropertyMock, side_effect=OSError
        ):
            with pytest.warns(UserWarning, match="RUNTIME_DIR not available"):
                path = store.runtime_dir
        assert path == cache_dir / "run"

    def test_cache_dir_not_affected_by_runtime_fallback(self):
        """Verify that runtime fallback doesn't corrupt other dirs."""
        store = LocalStorage("my-app")
        cache_before = store.cache_dir
        with patch.object(
            type(store._dirs), "user_runtime_dir", new_callable=PropertyMock, side_effect=OSError
        ):
            with pytest.warns(UserWarning):
                store.runtime_dir
        assert store.cache_dir == cache_before
