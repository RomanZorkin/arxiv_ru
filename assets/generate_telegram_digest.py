#!/usr/bin/env python3
"""Собирает telegram_digest.txt из digest.txt новых статей."""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path
from typing import List

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = PROJECT_ROOT / "articles"
NEW_ARTICLES_FILE = Path(__file__).resolve().parent / "new_article_ids.json"
TELEGRAM_DIGEST_FILE = Path(__file__).resolve().parent / "telegram_digest.txt"

TG_DIGEST_BOTTOM = """
---
Все переводы - https://github.com/RomanZorkin/arxiv_ru\n
💬 Обсуждение, предложения по переводу и замечания к материалам — как всегда в комментариях.
"""


def load_new_article_ids(path: Path) -> List[str]:
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    return [article_id.strip() for article_id in data.get("new_article_ids", []) if article_id.strip()]


def extract_telegram_block(digest_path: Path) -> str:
    with open(digest_path, encoding="utf-8") as f:
        lines_list = f.readlines()

    index = next((i for i, line in enumerate(lines_list) if "✏️" in line), -1)
    if index == -1:
        raise ValueError(f"Маркер ✏️ не найден в {digest_path}")

    return "".join(lines_list[index:])


def generate_telegram_digest(
    article_ids: List[str],
    week_publication: str | None = None,
    output_file: Path = TELEGRAM_DIGEST_FILE,
) -> str:
    if not article_ids:
        raise ValueError("Список статей пуст — нечего включать в дайджест.")

    publication_date = week_publication or date.today().strftime("%d.%m.%Y")

    tg_digest_title = f"""
🚀 Свежие переводы arXiv на русском от {publication_date}  
⏳ Страницы иногда могут открываться не очень быстро
---\n
"""

    digest_blocks: List[str] = []
    for article_id in article_ids:
        digest_path = ARTICLES_DIR / article_id / "digest.txt"
        if not digest_path.exists():
            raise FileNotFoundError(f"digest.txt не найден: {digest_path}")

        digest_blocks.append(extract_telegram_block(digest_path))
        print(f"✓ Добавлена в дайджест: {article_id}")

    digest_blocks.append(TG_DIGEST_BOTTOM)
    digest_text = tg_digest_title + "".join(digest_blocks)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(digest_text)

    print(f"\nГотово! Статей в дайджесте: {len(article_ids)}")
    print(f"Файл сохранён: {output_file.resolve()}")

    return digest_text


if __name__ == "__main__":
    try:
        ids = load_new_article_ids(NEW_ARTICLES_FILE)
        generate_telegram_digest(ids)
    except ValueError as e:
        print(f"⚠ {e}")
        print("Сначала запустите: python3 assets/update_knowledge_index.py")
        sys.exit(1)
    except (FileNotFoundError, OSError) as e:
        print(f"✗ {e}")
        sys.exit(1)
