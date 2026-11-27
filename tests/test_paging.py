import pytest

from pagekit.paging import page_count, page_slice, paginate


def test_page_count_exact():
    assert page_count(20, 10) == 2


def test_page_count_remainder():
    assert page_count(21, 10) == 3


def test_page_count_empty():
    assert page_count(0, 10) == 0


def test_page_count_rejects_zero_per_page():
    with pytest.raises(ValueError):
        page_count(5, 0)


def test_page_slice_first_page():
    assert page_slice(1, 10) == (0, 10)


def test_paginate_last_page():
    items = list(range(25))
    out = paginate(items, 3, 10)
    assert out["items"] == [20, 21, 22, 23, 24]
    assert out["pages"] == 3
    assert out["has_next"] is False
