import pandas as pd

def read_from_file() -> pd.DataFrame:
    """Read data from the Excel file 'data.xlsx' and return it as a DataFrame."""
    file_name = 'data.xlsx'
    data = pd.read_excel(file_name)
    return data

def write_to_file(content: pd.DataFrame) -> None:
    """Write data to the Excel file 'data.xlsx' from a DataFrame."""
    file_name = 'data.xlsx'
    content.to_excel(file_name, index=False)

if __name__ == "__main__":
    # Step 1: Read data from 'data.xlsx'
    data = read_from_file()
    print("Data read from 'data.xlsx':")
    print(data.head())  # Display the first few rows of the dataset
    
    # Step 2: Optionally write the data back to 'data.xlsx' or another file
    write_to_file(data)
    print("Data has been written back to 'data.xlsx'")

"""import csv

def read_from_file(file_name: str) -> list:
    data = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def write_to_file(file_name: str, content: list) -> None:
    if content:
        fieldnames = content[0].keys()
        with open(file_name, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(content) """ #if the dataset was in csv format
