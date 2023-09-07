import pandas as pd

# Define the data based on your description
data = {
    'Kingsford': [5 / 31, 3 / 31, 3 / 31, 31, 0.035],
    'Maroubra': [3 / 24, 1 / 24, 5 / 24, 24, 0.022],
    'Manly': [3 / 11, 2 / 11, 5 / 11, 11, 0.011],
    'Wollongong': [4 / 10, 2 / 10, 1 / 10, 10, -0.02],
    'CBD': [3 / 20, 11 / 200, 5 / 20, 20, 0.018],
    'Epping': [4 / 20, 22 / 200, 5 / 20, 20, 0.022],
    'Blacktown': [1 / 11, 9 / 11, 4 / 11, 11, 0.022],
    'Randwick': [2 / 10, 3 / 10, 6 / 10, 10, -0.042],
    'Average': [0.199990836, 0.225430108, 0.290411168, 17.125, 0.0085]
}

# Create a dataframe
df = pd.DataFrame(data, index=['gp', 'ep', 'specialist', 'population(k)', 'population growth'])


def avg(column):
    return sum(column) / len(column)


def ratio(df):
    return avg(df.loc['gp']), avg(df.loc['ep']), avg(df.loc['specialist'])


def prediction(population, growth, ratio):
    return round(population * (1 + growth) * ratio)


# Create a dataframe
city = 'Kingsford'
data = pd.DataFrame(data, index=['gp', 'ep', 'specialist', 'population(k)', 'population growth'], columns=[city])
# print(data)
gp_ratio, ep_ratio, specialist_ratio = ratio(data)
print(gp_ratio, ep_ratio, specialist_ratio)
city = data[city]
# print(city)
city.loc['expected_gp'] = prediction(city.loc['population(k)'], city.loc['population growth'], gp_ratio)
city.loc['expected_ep'] = prediction(city.loc['population(k)'], city.loc['population growth'], ep_ratio)
city.loc['expected_sp'] = prediction(city.loc['population(k)'], city.loc['population growth'], specialist_ratio)
print(city)

# Save dataframe to an Excel file
city.to_excel(f'{city}_data.xlsx')

print(f"Excel file '{city}_data.xlsx' has been created!")

# Save dataframe to an Excel file
df.to_excel('data.xlsx')

print("Excel file 'data.xlsx' has been created!")
