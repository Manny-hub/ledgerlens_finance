import json 
import hashlib
from datetime import datetime, timedelta

def read_jsonl(file_path) -> List[dict]:
    row = []
    for line in file_path.read().splitlines():
        line = line.strip()
        if not line:
            continue
        row.append(json.loads(line))
    return row

def stash_hash(parts: str) -> str:
    """Generate a hash for the given stash string."""
    raw = "|".join(parts).encode("utf-8")   
    return hashlib.sha256(raw).hexdigest()  # Generate a SHA256 hash of the JSON string


def parse_to_dt(str_dt: str) -> datetime:
    s = str_dt.replace("Z", "+00:00")
    dt = datetime.fromisoformat(s)  
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timedelta.utc)  # Set timezone to UTC if not provided
    return dt 

def to_utc(dt:datetime) -> datetime:
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timedelta.utc)  # Set timezone to UTC if not provided
    return dt.astimezone(timedelta.utc) 