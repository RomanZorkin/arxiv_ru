#!/usr/bin/env python3
"""Собирает readme_update.txt из digest.txt новых статей для обновления README."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import List, Tuple

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = PROJECT_ROOT / "articles"
NEW_ARTICLES_FILE = Path(__file__).resolve().parent / "new_article_ids.json"
README_UPDATE_FILE = Path(__file__).resolve().parent / "readme_update.txt"


def load_new_article_ids(path: Path) -> List[str]:
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    return [article_id.strip() for article_id in data.get("new_article_ids", []) if article_id.strip()]


def extract_readme_blocks(digest_path: Path) -> Tuple[str, str]:
    """Возвращает (блок «Последние статьи», строка таблицы «Архив»)."""
    with open(digest_path, encoding="utf-8") as f:
        content = f.read()

    parts = [part.strip() for part in content.split("---") if part.strip()]
    if len(parts) < 2:
        raise ValueError(f"Ожидается минимум 2 блока, разделённых '---': {digest_path}")

    return parts[0], parts[1]


def generate_readme_update(
    article_ids: List[str],
    output_file: Path = README_UPDATE_FILE,
) -> str:
    if not article_ids:
        raise ValueError("Список статей пуст — нечего включать в заготовку.")

    latest_blocks: List[str] = []
    archive_rows: List[str] = []

    for article_id in article_ids:
        digest_path = ARTICLES_DIR / article_id / "digest.txt"
        if not digest_path.exists():
            raise FileNotFoundError(f"digest.txt не найден: {digest_path}")

        latest_block, archive_row = extract_readme_blocks(digest_path)
        latest_blocks.append(latest_block)
        archive_rows.append(archive_row)
        print(f"✓ Добавлена: {article_id}")

    latest_section = "\n\n---\n\n".join(latest_blocks)
    archive_section = "\n".join(archive_rows)

    readme_text = f"""# Блок «Последние статьи»
# Вставить в README.md после заголовка «# 🔥 Последние статьи»

{latest_section}

---

# Строки таблицы «Архив статей»
# Вставить в README.md сразу после строки |---|---|---|---|---| (без пустой строки!)

{archive_section}
"""

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(readme_text)

    print(f"\nГотово! Статей в заготовке: {len(article_ids)}")
    print(f"Файл сохранён: {output_file.resolve()}")

    return readme_text


if __name__ == "__main__":
    try:
        ids = load_new_article_ids(NEW_ARTICLES_FILE)
        generate_readme_update(ids)
    except ValueError as e:
        print(f"⚠ {e}")
        print("Сначала запустите: python3 assets/update_knowledge_index.py")
        sys.exit(1)
    except (FileNotFoundError, OSError) as e:
        print(f"✗ {e}")
        sys.exit(1)
