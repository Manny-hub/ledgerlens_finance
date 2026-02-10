from __future__ import annotations
from typing import Any, Dict, List, Optional
from transfrom.timestamps import normalize_timestamp
from utils.commons import stash_hash

# Normalize app events by ensuring consistent timestamp formats and generating unique event IDs based on relevant fields. normalization + ID-stabilization function for analytics / event pipelines.

def normalize_app_event(row, default_tz: str = "UTC") -> Dict[str, Any]:
    
    # Event ID generation if exists or create a derterministic ID 
    event_id = row.get("event_id") or stash_hash(
        str(row.get("user_id")), 
        str(row.get("event_name", "")), 
        str(row.get("timestamp", "")),
        str(row.get("session_id", "")),
        )[:24] # Use the first 24 characters of the details to avoid excessively long hashes
    
    #Converts arbitrary timestamp formats into a normalized UTC datetim. Applies a default timezone if missing
    dt = normalize_timestamp(row.get("timestamp"), default_tz=default_tz) 
    
    # canonical field normalization and defaulting to empty strings for missing values. This ensures consistent data structure for downstream processing and analytics.
    return{
        "event_id": event_id,
        "event_name": (row.get("event_name") or "").lower().strip(),
        "user_id": str(row.get("user_id") or ""),
        "session_id": str(row.get("session_id") or ""),
        "order_id": str(row.get("order_id") or ""),
        "payment_intent_id": str(row.get("payment_intent_id") or ""),
        "event_ts_utc": dt,
        "country": (row.get("country") or "").upper().strip(),
        "device": (row.get("device") or "").lower().strip(),
        "utm_source": (row.get("utm_source") or ""),
        "utm_medium": (row.get("utm_medium") or ""),
        "utm_campaign": (row.get("utm_campaign") or ""),
        "raw": row,
    }