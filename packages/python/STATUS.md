# quanttide Python SDK — 状态报告

## 当前范围

仅包含 `storage` 模块（`LocalStorage` 类），`models` 等模块待开发。

## 验收结果

| 检查项 | 结果 |
|:------|:----|
| API 可用 | ✅ 6 个属性全部实现 |
| 环境变量覆写 | ✅ 6 个类别均支持 |
| 编译构建 | ✅ `hatchling build` 通过 |
| 类型标记 | ✅ `py.typed` 已放置 |
| 测试总数 | ✅ 14 个，全部通过 |
| 覆盖率 | ✅ 100%（含异常分支） |

## 已知问题

| # | 问题 | 文件 | 影响 | 状态 |
|---|------|------|------|------|
| 1 | `pyproject.toml` 的 `readme` 指向空 `README.md`，实际文档在 `docs/README.md` | `pyproject.toml:5` | PyPI 展示为空 | ✅ 已修复（`docs/README.md` 已合并到根 `README.md`） |
| 2 | 测试仅验证返回值类型和名字包含，未覆盖 `PermissionError` 和 `OSError` 异常分支 | `tests/test_storage.py` | 回归防护弱 | ✅ 已修复（100% 覆盖率） |
| 3 | 环境变量测试用 `del os.environ` 清理，异常中断时会污染环境 | `tests/test_storage.py:56-68` | 测试隔离性弱 | 🟡 待修复（改用 `monkeypatch`） |
| 4 | `pyproject.toml` 缺少 `[project.urls]` 和 `keywords` 等 PyPI 元信息 | `pyproject.toml` | PyPI 展示不完整 | 🟢 低优 |

## 文件结构

```
src/quanttide/
  __init__.py       # 导出 LocalStorage
  storage.py        # LocalStorage 实现
  py.typed          # PEP 561 类型标记
tests/
  __init__.py
  test_storage.py   # 14 个测试
pyproject.toml      # 项目配置
README.md           # 使用文档（合并自 docs/README.md）
STATUS.md           # 本文件
TODO.md             # 待办事项
```
