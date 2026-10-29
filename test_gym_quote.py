
"""Unit tests for the gym membership quotation system."""

import pytest

from gym_quote import GymQuote


def test_basic_plan_price():
    """Verify the BASIC membership price."""
    quote = GymQuote()

    assert quote.get_plan_price("BASIC") == 30


def test_invalid_plan():
    """Verify that an unknown plan is rejected."""
    quote = GymQuote()

    with pytest.raises(ValueError):
        quote.get_plan_price("GOLD")

@pytest.mark.parametrize(
    "plan, expected_price",
    [
        ("BASIC", 30),
        ("STANDARD", 45),
        ("PREMIUM", 70),
    ],
)
def test_plan_prices(plan, expected_price):
    """Verify the price of each membership plan."""
    quote = GymQuote()

    assert quote.get_plan_price(plan) == expected_price
