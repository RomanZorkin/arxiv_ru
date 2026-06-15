# Скрипты публикации arxiv_ru

Утилиты для обновления индекса, подготовки дайджестов и проверки согласованности после загрузки новых статей в `articles/`.

Запускать из корня репозитория через [uv](https://docs.astral.sh/uv/):

```bash
uv run assets/<скрипт>.py
```

Скрипты используют только стандартную библиотеку Python, отдельные зависимости не нужны.

---

## Единый старт (рекомендуется)

```bash
uv run assets/run_pipeline.py
```

Выполняет по порядку:

1. `update_knowledge_index.py` → `knowledge_index.json`, `new_article_ids.json`
2. `generate_telegram_digest.py` → `telegram_digest.txt` *(только если есть новые статьи)*
3. `generate_readme_update.py` → `readme_update.txt` *(только если есть новые статьи)*
4. `check_articles_consistency.py` → проверка `articles/` ↔ индекс ↔ README

Код выхода: `0` — всё в порядке, `1` — ошибка или расхождения.

---

## Скрипты по отдельности

| Скрипт | Назначение | Результат |
|--------|------------|-----------|
| `update_knowledge_index.py` | Собирает индекс из `articles/*/metadata.json` | `knowledge_index.json`, `new_article_ids.json` |
| `generate_telegram_digest.py` | Дайджест для Telegram из `digest.txt` | `telegram_digest.txt` |
| `generate_readme_update.py` | Заготовка для README из `digest.txt` | `readme_update.txt` |
| `check_articles_consistency.py` | Сверка всех ID в индексе и таблице README | отчёт в консоль |

Пример пошагового запуска:

```bash
uv run assets/update_knowledge_index.py
uv run assets/generate_telegram_digest.py
uv run assets/generate_readme_update.py
# вручную вставить блоки из readme_update.txt в README.md
uv run assets/check_articles_consistency.py
```

---

## Генерируемые файлы

| Файл | Описание |
|------|----------|
| `new_article_ids.json` | Список ID статей, добавленных с прошлого обновления индекса |
| `telegram_digest.txt` | Текст для публикации в Telegram |
| `readme_update.txt` | Блок «Последние статьи» + строки таблицы «Архив статей» |

---

## Требования к статье

В каталоге `articles/<arxiv_id>/` должны быть:

- `metadata.json` — заголовки, теги, дата перевода
- `digest.txt` — три блока через `---`: README-карточка, строка таблицы, блок для Telegram (`✏️`)

Без заголовков в `metadata.json` статья не попадёт в индекс.
