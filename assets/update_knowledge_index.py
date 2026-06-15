#!/usr/bin/env python3
"""Обновляет knowledge_index.json по metadata.json из articles/."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Dict, List, Set, Tuple

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = PROJECT_ROOT / "articles"
INDEX_FILE = PROJECT_ROOT / "knowledge_index.json"
NEW_ARTICLES_FILE = Path(__file__).resolve().parent / "new_article_ids.json"


def load_existing_ids(index_path: Path) -> Set[str]:
    if not index_path.exists():
        return set()
    with open(index_path, encoding="utf-8") as f:
        data = json.load(f)
    return {article["id"].strip() for article in data.get("articles", [])}


def publication_month_from_id(article_id: str) -> str:
    """arxiv id YYMM.xxxxx -> MM.20YY"""
    return f"{article_id[2:4]}.20{article_id[0:2]}"


def generate_arxiv_index(base_dir: Path, output_file: Path) -> Tuple[Dict, List[str]]:
    base_path = base_dir.resolve()

    if not base_path.exists():
        raise FileNotFoundError(f"Папка не найдена: {base_path}")

    existing_ids = load_existing_ids(output_file)
    articles: List[Dict] = []

    print(f"Начинаем обработку папки: {base_path}")

    for meta_path in base_path.rglob("metadata.json"):
        try:
            with open(meta_path, encoding="utf-8") as f:
                meta = json.load(f)

            article_id = meta_path.parent.name.strip()
            rel_path = meta_path.parent.relative_to(base_path)

            article = {
                "id": article_id,
                "path": f"articles/{rel_path}/",
                "readme": f"articles/{rel_path}/README.md",
                "publication_month": publication_month_from_id(article_id),
                "translation_date": meta.get("created_at"),
                "title_ru": meta.get("title_ru"),
                "title_en": meta.get("title_en"),
                "tags": meta.get("tags", []),
                "has_manual_review": meta.get("has_manual_review", False),
            }

            if article.get("title_ru") or article.get("title_en"):
                articles.append(article)
                print(f"✓ Добавлена: {article_id}")
            else:
                print(f"⚠ Пропущена (нет заголовка): {article_id}")

        except Exception as e:
            print(f"✗ Ошибка при обработке {meta_path}: {e}")

    articles.sort(key=lambda x: x["id"])
    new_article_ids = [article["id"] for article in articles if article["id"] not in existing_ids]

    index_data = {
        "project": "arxiv_ru",
        "description": (
            "Semantic index of translated arXiv papers with metadata optimized "
            "for LLM navigation, RAG retrieval and research exploration."
        ),
        "schema_version": "1.0",
        "total_articles": len(articles),
        "generated_at": date.today().isoformat(),
        "articles": articles,
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)

    new_articles_data = {
        "generated_at": date.today().isoformat(),
        "total_new": len(new_article_ids),
        "new_article_ids": new_article_ids,
    }
    with open(NEW_ARTICLES_FILE, "w", encoding="utf-8") as f:
        json.dump(new_articles_data, f, ensure_ascii=False, indent=2)

    print(f"\nГотово! Обработано статей: {len(articles)}")
    print(f"Новых статей: {len(new_article_ids)}")
    if new_article_ids:
        print("ID новых статей:", ", ".join(new_article_ids))
    else:
        print("Новых статей не обнаружено.")
    print(f"Индекс сохранён: {output_file.resolve()}")
    print(f"Список новых ID: {NEW_ARTICLES_FILE.resolve()}")

    return index_data, new_article_ids


if __name__ == "__main__":
    generate_arxiv_index(ARTICLES_DIR, INDEX_FILE)
