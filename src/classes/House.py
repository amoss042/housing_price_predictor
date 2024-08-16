#OOP
class House:
    def __init__(self, house_id, neighborhood, house_style, overall_condition, year_built, roof_type,
                 roof_material, foundation_material, heating, central_air, electrical, fireplace_num,
                 garage_area, date_sold):
        self.house_id = house_id
        self.neighborhood = neighborhood
        self.house_style = house_style
        self.overall_condition = overall_condition
        self.year_built = year_built
        self.roof_type = roof_type
        self.roof_material = roof_material
        self.foundation_material = foundation_material
        self.heating = heating
        self.central_air = central_air
        self.electrical = electrical
        self.fireplace_num = fireplace_num
        self.garage_area = garage_area
        self.date_sold = date_sold

    def update(self, updated_fields: dict) -> None:
        """Update the fields of the house instance."""
        for field, value in updated_fields.items():
            if hasattr(self, field):
                setattr(self, field, value)

# Dictionary to store House instances
houses = {}

#data manipulation
def add_house(house: House) -> None:
    """Add a new House instance to the dictionary."""
    houses[house.house_id] = house

def get_house_by_id(house_id: int) -> House:
    """Retrieve a House instance by its ID."""
    return houses.get(house_id)

def update_house_by_id(house_id: int, updated_fields: dict) -> None:
    """Update the fields of an existing House instance by its ID."""
    house = houses.get(house_id)
    if house:
        house.update(updated_fields)

def delete_house_by_id(house_id: int) -> None:
    """Delete a House instance from the dictionary by its ID."""
    if house_id in houses:
        del houses[house_id]

def get_houses_by_filters(filters: dict) -> list:
    """Retrieve a list of House instances that match the given filters."""
    result = []
    for house in houses.values():
        match = True
        for field, value in filters.items():
            if getattr(house, field, None) != value:
                match = False
                break
        if match:
            result.append(house)
    return result
