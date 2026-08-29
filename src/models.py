from dataclasses import dataclass
from typing import Optional


@dataclass
class Job:
    company: str
    role: str
    location: str
    source_url: str
    date_posted: Optional[str] = None
    status: str = "UNKNOWN"
    fit_score: Optional[int] = None
    priority: Optional[str] = None
