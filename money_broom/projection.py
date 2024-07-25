from typing import List

from money_broom.enums import ProjectionEndEnum
from money_broom.models import Projection, ProjectionStep


def project(
    base: float,
    interest_rate: float,
    deposit: float | List[float],
    period_limit: None | ProjectionEndEnum = None,
) -> Projection:
    steps: List[ProjectionStep] = []

    initial_amount = base

    annual_interest_rate = interest_rate
    monthly_interest_rate = (1 + interest_rate) ** (1 / 12) - 1

    cumulative_amount = base
    cumulative_deposit_amount = 0
    cumulative_interest_amount = 0

    for i in range(period_limit):
        step_amount = cumulative_amount
        step_interest_amount = cumulative_amount * monthly_interest_rate
        step_deposit_amount = deposit

        cumulative_amount += cumulative_amount * monthly_interest_rate + deposit

        # if i > 0:
        #     cumulative_amount += cumulative_amount * monthly_interest_rate + deposit
        # else:
        #     cumulative_amount += cumulative_amount * monthly_interest_rate

        # cumulative_amount = cumulative_amount + cumulative_amount * monthly_interest_rate + deposit
        step = ProjectionStep(
            cumulative_amount,
            cumulative_interest_amount,
            cumulative_deposit_amount,
            step_amount,
            step_interest_amount,
            step_deposit_amount,
        )
        steps.append(step)

    return Projection(
        initial_amount,
        cumulative_amount,
        cumulative_deposit_amount,
        annual_interest_rate,
        len(steps),
        steps,
    )
