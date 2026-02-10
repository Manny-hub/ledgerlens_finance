from __future__ import annotations
from typing import Any, Dict, List, Optional
from utils.commons import parse_to_dt, to_utc


def normalize_timestamps(ts: str | None, default_tz: str = "UTC") -> datetime | None:
    if not ts:
       return None
    try: 
        dt = parse_to_dt(ts, default_tz=default_tz)
        dt = to_utc(dt)
        return dt
    except Exception:
            return None