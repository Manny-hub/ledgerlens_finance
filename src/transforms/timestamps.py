from __future__ import annotations
from typing import Any, Dict, List, Optional
from utils.commons import parse_to_dt, to_utc


def normalize_timestamps(ts: str | None, default_tz: str = "UTC") -> datetime | None:
    if not ts:
       return None
    try: 
        return to_utc(parse_to_dt(ts, default_tz=default_tz))
    except Exception:
            return None