
"""Gym membership quotation system."""


class GymQuote:
    """Represent a gym membership quotation."""

    PLAN_PRICES = {
        "BASIC": 30,
        "STANDARD": 45,
        "PREMIUM": 70,
    }

    def get_plan_price(self, plan):
        """Return the monthly price of a valid plan."""
        if plan not in self.PLAN_PRICES:
            raise ValueError("Invalid membership plan.")

        return self.PLAN_PRICES[plan]
