from money_broom.models import ProjectionStep
from money_broom.projection import project


class TestInvestment:
    def test_simple_investment(self):
        # Arrange
        initial_deposit = 10000
        monthly_deposit = 100
        interest_rate = 0.104
        monthly_interest_rate = (1 + interest_rate) ** (1 / 12) - 1
        projection_period = 12

        mock_steps = [
            ProjectionStep(10000.0, 0.1, 100.0, 10000.0, 0.1, 100.0),
            ProjectionStep(10000.0, 0.1, 100.0, 10000.0, 0.1, 100.0),
            ProjectionStep(10000.0, 0.1, 100.0, 10000.0, 0.1, 100.0),
            ProjectionStep(10000.0, 0.1, 100.0, 10000.0, 0.1, 100.0),
            ProjectionStep(10000.0, 0.1, 100.0, 10000.0, 0.1, 100.0),
            ProjectionStep(10000.0, 0.1, 100.0, 10000.0, 0.1, 100.0),
            ProjectionStep(10000.0, 0.1, 100.0, 10000.0, 0.1, 100.0),
            ProjectionStep(10000.0, 0.1, 100.0, 10000.0, 0.1, 100.0),
            ProjectionStep(10000.0, 0.1, 100.0, 10000.0, 0.1, 100.0),
            ProjectionStep(10000.0, 0.1, 100.0, 10000.0, 0.1, 100.0),
            ProjectionStep(10000.0, 0.1, 100.0, 10000.0, 0.1, 100.0),
            ProjectionStep(10000.0, 0.1, 100.0, 10000.0, 0.1, 100.0),
        ]

        # Act
        projection = project(initial_deposit, interest_rate, monthly_deposit, projection_period)

        # Assert
        assert projection.intial_amount == 10000
        assert round(projection.final_amount, 2) == 12296.18
        # assert projection.final_deposit_amount == 11200.0
        # assert projection.final_interest_amount == 123
        # assert projection.total_steps == 12
        # for step, mock_step in zip(projection.steps, mock_steps):
        #     step.amount == mock_step.amount
        #     step.deposit == mock_step.deposit
        #     step.interest == mock_step.interest
