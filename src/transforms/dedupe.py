from __future__ import annotations
from typing import Any, Dict, List, Optional

# Dedupe a list of dictionaries based on a specified key or the entire dictionary if no key is provided.

def dedupe_dicts(rows: list[dict], key: str | None = None) -> list[dict]:
    seen = set() # To track seen identifiers (either based on the specified key or the entire dictionary)
    out = []   # To store the deduplicated list of dictionaries

    for d in rows: 
        if key is not None and key in d:
            identifier = d[key] # 
        else:
            identifier = tuple(sorted(d.items()))  # Use the entire dictionary as the identifier by converting it to a sorted tuple of items

        if identifier not in seen: # If the identifier has not been seen before, add it to the seen set and include the dictionary in the output list
            seen.add(identifier)
            out.append(d)

    return out
