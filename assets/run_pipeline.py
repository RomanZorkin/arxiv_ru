#!/usr/bin/env python3
"""Единая точка запуска: индекс → дайджест → README → проверка."""

from __future__ import annotations

import sys
from pathlib import Path

ASSETS_DIR = Path(__file__).resolve().parent
if str(ASSETS_DIR) not in sys.path:
    sys.path.insert(0, str(ASSETS_DIR))

from check_articles_consistency import check_consistency, print_report
from generate_readme_update import generate_readme_update
from generate_telegram_digest import generate_telegram_digest
from update_knowledge_index import ARTICLES_DIR, INDEX_FILE, generate_arxiv_index


def print_step(step: int, total: int, title: str) -> None:
    print()
    print("=" * 60)
    print(f"{step}/{total} {title}")
    print("=" * 60)


def main() -> int:
    total_steps = 4

    print_step(1, total_steps, "Обновление knowledge_index.json")
    try:
        _, new_article_ids = generate_arxiv_index(ARTICLES_DIR, INDEX_FILE)
    except (FileNotFoundError, OSError) as e:
        print(f"✗ {e}")
        return 1

    if new_article_ids:
        print_step(2, total_steps, "Генерация telegram_digest.txt")
        try:
            generate_telegram_digest(new_article_ids)
        except (FileNotFoundError, OSError, ValueError) as e:
            print(f"✗ {e}")
            return 1

        print_step(3, total_steps, "Генерация readme_update.txt")
        try:
            generate_readme_update(new_article_ids)
        except (FileNotFoundError, OSError, ValueError) as e:
            print(f"✗ {e}")
            return 1
    else:
        print()
        print("⚠ Новых статей нет — шаги 2 и 3 пропущены (дайджест и README).")

    print_step(4, total_steps, "Проверка согласованности")
    try:
        report = check_consistency()
        print_report(report)
    except (FileNotFoundError, OSError) as e:
        print(f"✗ {e}")
        return 1

    print()
    if report["ok"]:
        print("✓ Pipeline завершён успешно.")
        return 0

    print("✗ Pipeline завершён с ошибками согласованности.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
