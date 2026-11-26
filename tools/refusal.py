"""Detect output-filter or recitation-filter refusals in model replies so tools switch cleanly to ocr_fallback.py."""

MARKERS = (
    "content filtering policy",
    "output blocked",
    "recitation",
    "finish_reason: recitation",
    "copyrighted material",
    "cannot reproduce verbatim",
)


def is_refusal(msg):
    s = (msg or "").lower()
    return any(m in s for m in MARKERS)
