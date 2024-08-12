import pytest

def predict_price(house_data):
    """
    Predicts the price of a house based on historical data.

    Args:
        house_data (dict): A dictionary containing features of the house such as 
                           number of bedrooms, square footage, location, etc.

    Returns:
        float: The predicted price of the house.

    Raises:
        TypeError: If the input is not a dictionary.
    """
    if not isinstance(house_data, dict):
        raise TypeError("house_data must be a dictionary")
    
    # Dummy implementation
    return 250000.0

def test_predict_price():
    """
    Tests the predict_price function with various scenarios.
    """

    # Normal case
    assert predict_price({'bedrooms': 3, 'square_footage': 2000, 'location': 'city_center'}) == 250000.0

    # Edge case with zero square footage
    assert predict_price({'bedrooms': 3, 'square_footage': 0, 'location': 'city_center'}) == 250000.0

    # Edge case with missing data
    assert predict_price({'bedrooms': 3}) == 250000.0

    # Error case with non-dict input
    with pytest.raises(TypeError):
        predict_price(1234)
