import pandas as pd

# Define the data based on your description
data = {
    'Kingsford':    [5/31, 3/31, 3/31, 31, 0.035],
    'Maroubra':     [3/24, 1/24, 5/24, 24, 0.022],
    'Manly':        [3/11, 2/11, 5/11, 11, 0.011],
    'Wollongong':   [4/10, 2/10, 1/10, 10, -0.02],
    'CBD':          [3/20, 11/200, 5/20, 20, 0.018],
    'Epping':       [4/20, 22/200, 5/20, 20, 0.022],
    'Blacktown':    [1/11, 9/11, 4/11, 11, 0.022],
    'Randwick':     [2/10, 3/10, 6/10, 10, -0.042],
    #'Average' :     []
}

# Create a dataframe
df = pd.DataFrame(data, index=['gp', 'ep', 'specialist', 'population(k)', 'population growth'])

# Save dataframe to an Excel file
df.to_excel('data.xlsx')

print("Excel file 'data.xlsx' has been created!")
