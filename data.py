import pandas as pd

# Define the data based on your description
data = {
    'Kingsford': [5, 3, 3],
    'Maroubra': [3, 8, 5],
    'Randwick': [2, 3, 6]
}

# Create a dataframe
df = pd.DataFrame(data, index=['gp', 'ep', 'specialist'])

# Save dataframe to an Excel file
df.to_excel('data.xlsx')

print("Excel file 'data.xlsx' has been created!")
