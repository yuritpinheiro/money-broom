from dataclasses import dataclass
from typing import List

from money_broom.enums import PeriodEnum


@dataclass
class ExtraTax:
    name: str
    value: float


@dataclass
class Financing:
    principal: float
    limit: int
    interest: float
    extra_taxes: float | List[ExtraTax]


@dataclass
class Investment:
    amount: float
    interest_rate: float
    period: PeriodEnum


@dataclass
class ProjectionStep:
    cumulative_amount: float
    cumulative_interest: float
    cumulative_deposit: float
    step_amount: float
    step_interest: float
    step_deposit: float


@dataclass
class Projection:
    intial_amount:float
    final_amount: float
    final_deposit_amount: float
    final_interest_amount: float
    total_steps: int
    steps: List[ProjectionStep]
