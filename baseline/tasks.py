"""Lesson 4 homework: baseline tasks.

Replace each `raise NotImplementedError` with your implementation.
You may use AI, as long as you can explain every line.
"""
import json


def count_selected(media_ids: list[str]) -> int:
    return len(set(media_ids))


def group_by_gallery(media: list[dict]) -> dict[str, list[str]]:
    return {gallery["gallery_id"]: [item["id"] for item in media if item["gallery_id"] == gallery["gallery_id"]] for gallery in media}

def total_price(prices_minor: list[int | None]) -> int:
    return sum(price for price in prices_minor if price is not None)


def first_missing(required: list[str], present: list[str]) -> str | None:
    return next((item for item in required if item not in present), None)


def load_events(path) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
