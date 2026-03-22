from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Company:
    name: str
    ticker: Optional[str] = None
    id: Optional[int] = None

@dataclass
class Analysis:
    company_id: int
    raw_content: str
    source_url: Optional[str] = None
    ai_summary: Optional[str] = None
    priority_score: Optional[float] = None
    collection_date: Optional[datetime] = None
    id: Optional[int] = None

@dataclass
class User:
    name: str
    email: str
    created_at: Optional[datetime] = None
    id: Optional[int] = None

@dataclass
class EvaluationParameter:
    parameter_name: str
    weight: float
    description: Optional[str] = None
    id: Optional[int] = None