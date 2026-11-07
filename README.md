# ЛР 9. Запуск автотестов в CI (GitHub Actions)

Автотесты из предыдущих лабораторных запускаются автоматически
при каждом push в ветку `main`.

| Папка | Что внутри | Тестов |
|---|---|---|
| `tests/unit` | модульные тесты класса `Calculator` (ЛР 6) | 46 |
| `tests/api` | тесты REST API JSONPlaceholder на `requests` (ЛР 5) | 9 |

Workflow: `.github/workflows/run-tests.yml` — Ubuntu, Python 3.12,
установка зависимостей из `requirements.txt`, запуск `pytest`.

## Локальный запуск (Windows, PowerShell)

```
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -v
```
