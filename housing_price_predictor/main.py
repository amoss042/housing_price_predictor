def calculate_average_neighbor_price(neighbor_prices):
    """
    Calculates the average price of neighboring houses.

    Args:
        neighbor_prices (list of float): A list of prices for neighboring houses.

    Returns:
        float: The average price of the neighboring houses.

    Raises:
        ValueError: If the neighbor_prices list is empty.
    """
    if not neighbor_prices:
        raise ValueError("The neighbor_prices list cannot be empty.")
    
    return sum(neighbor_prices) / len(neighbor_prices)
