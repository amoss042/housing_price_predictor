import sys
import os
import pytest
import pandas as pd

# Update the path to include the src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from classes.house import House, houses, add_house, get_house_by_id, update_house_by_id, delete_house_by_id, get_houses_by_filters
from utils.file_io import read_from_file, write_to_file  # Importing the functions

# Test data setup
@pytest.fixture
def setup_data():
    # Create some test House instances
    house1 = House(1, 'Neighborhood A', '1Story', 'Good', 2005, 'Gable', 'CompShg', 'PConc', 'GasA', 'Y', 'SBrkr', 2, 500, '05/2021')
    house2 = House(2, 'Neighborhood B', '2Story', 'Excellent', 2010, 'Hip', 'Metal', 'Slab', 'Electric', 'N', 'Fuse', 1, 300, '06/2022')
    houses[house1.house_id] = house1
    houses[house2.house_id] = house2
    return house1, house2

# Test add_house function
def test_add_house(setup_data):
    house3 = House(3, 'Neighborhood C', 'Split', 'Fair', 1999, 'Gable', 'Wood', 'Basement', 'GasA', 'Y', 'SBrkr', 1, 200, '07/2023')
    add_house(house3)
    assert houses[house3.house_id] == house3

# Test get_house_by_id function
def test_get_house_by_id(setup_data):
    house1, _ = setup_data
    retrieved_house = get_house_by_id(house1.house_id)
    assert retrieved_house == house1

# Test update_house_by_id function
def test_update_house_by_id(setup_data):
    house1, _ = setup_data
    updated_fields = {'neighborhood': 'Updated Neighborhood', 'year_built': 2021}
    update_house_by_id(house1.house_id, updated_fields)
    updated_house = houses[house1.house_id]
    assert updated_house.neighborhood == 'Updated Neighborhood'
    assert updated_house.year_built == 2021

# Test delete_house_by_id function
def test_delete_house_by_id(setup_data):
    house1, _ = setup_data
    delete_house_by_id(house1.house_id)
    assert house1.house_id not in houses

# Test get_houses_by_filters function
def test_get_houses_by_filters(setup_data):
    _, house2 = setup_data
    filters = {'neighborhood': 'Neighborhood B', 'house_style': '2Story'}
    filtered_houses = get_houses_by_filters(filters)
    assert len(filtered_houses) == 1
    assert filtered_houses[0] == house2
