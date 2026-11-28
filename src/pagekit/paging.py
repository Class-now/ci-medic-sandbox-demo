"""Pagination helpers used by the sandbox API."""

from __future__ import annotations

import math


def page_count(total: int, per_page: int) -> int:
    """Number of pages needed to show `total` items, `per_page` at a time."""
    if per_page <= 0:
        raise ValueError("per_page must be positive")
    if total <= 0:
        return 0
    return total // per_page


def page_slice(page: int, per_page: int) -> tuple[int, int]:
    """Start and end index (end exclusive) of 1-based `page`."""
    if page < 1:
        raise ValueError("page is 1-based")
    start = (page - 1) * per_page
    return start, start + per_page


def paginate(items: list, page: int, per_page: int) -> dict:
    start, end = page_slice(page, per_page)
    return {
        "page": page,
        "pages": page_count(len(items), per_page),
        "items": items[start:end],
        "has_next": end < len(items),
    }
