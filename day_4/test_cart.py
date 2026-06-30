import pytest
from cart import calculate_total

@pytest.fixture
def sample_item_prices():
    """Generates sample prices for tests"""
    return [10.00, 20.50, 5.00]

# check for regular discount on a cart
def test_total_standard(sample_item_prices):
    # item_prices = [10.00, 20.50, 5.00]
    result = calculate_total(sample_item_prices, 0.10)
    assert result == 31.95
    
# check for empty cart
def test_empty_cart():
    result = calculate_total([])
    assert result == 0.0

# check for errors being raised
def test_total_invalid_discount(sample_item_prices):
    with pytest.raises(ValueError):
        calculate_total(sample_item_prices, 1.5)
