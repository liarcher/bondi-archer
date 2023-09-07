import pandas as pd

# Define the data based on your description
data = {
    'Kingsford': [5, 3, 3, 31, 3.5],
    'Maroubra': [3, 1, 5, 24, 2.2],
    'Manly': [3, 2, 5, 11, 1.1],
    'Wollongong': [4, 2, 1, 10, -0.2],
    'CBD': [3, 8, 5, 20, 1.8],
    'Epping': [3, 8, 5, 20, 2.2],
    'Blacktown': [3, 8, 5, 11, 2.2],
    'Randwick': [2, 3, 6, 10, -4.2]
}

# Create a dataframe
df = pd.DataFrame(data, index=['gp', 'ep', 'specialist', 'population(k)', 'population growth'])

# Save dataframe to an Excel file
df.to_excel('data.xlsx')

print("Excel file 'data.xlsx' has been created!")
