#!/usr/bin/env python3
"""Проверяет, что все статьи из articles/ есть в knowledge_index.json и в README «Архив статей»."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = PROJECT_ROOT / "articles"
INDEX_FILE = PROJECT_ROOT / "knowledge_index.json"
README_FILE = PROJECT_ROOT / "README.md"

ARXIV_ID_RE = re.compile(r"^\d{4}\.\d{5}$")
README_ARCHIVE_ROW_RE = re.compile(r"^\|\s*\[(\d{4}\.\d{5})\]")


def collect_article_ids_from_disk(articles_dir: Path) -> Set[str]:
    ids: Set[str] = set()
    for meta_path in articles_dir.rglob("metadata.json"):
        article_id = meta_path.parent.name.strip()
        if ARXIV_ID_RE.match(article_id):
            ids.add(article_id)
    return ids


def load_index_ids(index_path: Path) -> Set[str]:
    with open(index_path, encoding="utf-8") as f:
        data = json.load(f)
    return {article["id"].strip() for article in data.get("articles", [])}


def load_readme_archive_ids(readme_path: Path) -> Tuple[Set[str], List[str]]:
    with open(readme_path, encoding="utf-8") as f:
        lines = f.readlines()

    archive_started = False
    ids: Set[str] = set()
    duplicates: List[str] = []

    for line in lines:
        if line.strip() == "## Архив статей":
            archive_started = True
            continue
        if not archive_started:
            continue
        if not line.startswith("|"):
            if ids:
                break
            continue
        if line.startswith("|---"):
            continue

        match = README_ARCHIVE_ROW_RE.match(line)
        if not match:
            continue

        article_id = match.group(1)
        if article_id in ids:
            duplicates.append(article_id)
        ids.add(article_id)

    return ids, duplicates


def format_id_list(ids: Set[str]) -> str:
    return ", ".join(sorted(ids)) if ids else "—"


def check_consistency() -> Dict[str, object]:
    if not ARTICLES_DIR.exists():
        raise FileNotFoundError(f"Папка не найдена: {ARTICLES_DIR}")
    if not INDEX_FILE.exists():
        raise FileNotFoundError(f"Файл не найден: {INDEX_FILE}")
    if not README_FILE.exists():
        raise FileNotFoundError(f"Файл не найден: {README_FILE}")

    disk_ids = collect_article_ids_from_disk(ARTICLES_DIR)
    index_ids = load_index_ids(INDEX_FILE)
    readme_ids, readme_duplicates = load_readme_archive_ids(README_FILE)

    missing_in_index = disk_ids - index_ids
    extra_in_index = index_ids - disk_ids
    missing_in_readme = disk_ids - readme_ids
    extra_in_readme = readme_ids - disk_ids

    ok = not any([missing_in_index, extra_in_index, missing_in_readme, extra_in_readme, readme_duplicates])

    return {
        "ok": ok,
        "disk_total": len(disk_ids),
        "index_total": len(index_ids),
        "readme_total": len(readme_ids),
        "missing_in_index": missing_in_index,
        "extra_in_index": extra_in_index,
        "missing_in_readme": missing_in_readme,
        "extra_in_readme": extra_in_readme,
        "readme_duplicates": readme_duplicates,
    }


def print_report(result: Dict[str, object]) -> None:
    print("Проверка согласованности статей")
    print(f"  articles/ (metadata.json): {result['disk_total']}")
    print(f"  knowledge_index.json:        {result['index_total']}")
    print(f"  README «Архив статей»:     {result['readme_total']}")
    print()

    issues = False

    if result["missing_in_index"]:
        issues = True
        print("✗ Нет в knowledge_index.json:")
        print(f"  {format_id_list(result['missing_in_index'])}")

    if result["extra_in_index"]:
        issues = True
        print("✗ Лишние ID в knowledge_index.json (нет папки в articles/):")
        print(f"  {format_id_list(result['extra_in_index'])}")

    if result["missing_in_readme"]:
        issues = True
        print("✗ Нет в README «Архив статей»:")
        print(f"  {format_id_list(result['missing_in_readme'])}")

    if result["extra_in_readme"]:
        issues = True
        print("✗ Лишние ID в README «Архив статей» (нет папки в articles/):")
        print(f"  {format_id_list(result['extra_in_readme'])}")

    if result["readme_duplicates"]:
        issues = True
        print("✗ Дубликаты строк в README «Архив статей»:")
        print(f"  {', '.join(result['readme_duplicates'])}")

    if not issues:
        print("✓ Все ID из articles/ присутствуют в knowledge_index.json и в README.")


if __name__ == "__main__":
    try:
        report = check_consistency()
        print_report(report)
        sys.exit(0 if report["ok"] else 1)
    except (FileNotFoundError, json.JSONDecodeError, OSError) as e:
        print(f"✗ {e}")
        sys.exit(1)
