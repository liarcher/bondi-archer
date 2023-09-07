from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

excel_file = 'data.xlsx'  # Data input

# df = pd.read_excel(excel_file, usecols=range(1, 5))
data = {
    'Kingsford': [5 / 31, 3 / 31, 3 / 31, 31, 0.035],
    'Maroubra': [3 / 24, 1 / 24, 5 / 24, 24, 0.022],
    'Manly': [3 / 11, 2 / 11, 5 / 11, 11, 0.011],
    'Wollongong': [4 / 10, 2 / 10, 1 / 10, 10, -0.02],
    'CBD': [3 / 20, 11 / 200, 5 / 20, 20, 0.018],
    'Epping': [4 / 20, 22 / 200, 5 / 20, 20, 0.022],
    'Blacktown': [1 / 11, 9 / 11, 4 / 11, 11, 0.022],
    'Randwick': [2 / 10, 3 / 10, 6 / 10, 10, 0.000],
    'Average': [0.199990836, 0.225430108, 0.290411168, 17.125, 0.0185]
}

# Create a dataframe
df = pd.DataFrame(data, index=['gp', 'ep', 'specialist', 'population(k)', 'population growth'])


@app.route('/')
def index():
    return render_template('index2.html')


def avg(column):
    return sum(column) / len(column)


def ratio(df):
    print(df.keys())
    return avg(df.loc['gp']), avg(df.loc['ep']), avg(df.loc['specialist'])


def prediction(population, growth, ratio, real_gp_ratio, name):
    return '{}     Current {}: {}'.format(round(population * (1 + growth) * ratio), name, round(population * real_gp_ratio))
    # return ','.join(map(str,[round(population * (1 + growth) * ratio),'   Current GP:', population * real_gp_ratio]))


@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    location = request.form.get('location')
    gp_ratio, ep_ratio, sp_ratio = ratio(df)

    if location in df.columns:

        data = df[location].to_dict()
        labels = list(data.keys())
        values = list(data.values())
        expected_gp = prediction(df[location].loc['population(k)'], df[location].loc['population growth'],
                                 gp_ratio, df[location].loc['gp'], 'GP')

        expected_ep = prediction(df[location].loc['population(k)'], df[location].loc['population growth'],
                                 ep_ratio, df[location].loc['ep'], 'EP')

        expected_sp = prediction(df[location].loc['population(k)'], df[location].loc['population growth'],
                                 sp_ratio, df[location].loc['specialist'], 'Specialist')
        return jsonify({
            'labels': labels,
            'values': values,
            'expected_gp': expected_gp,
            'expected_ep': expected_ep,
            'expected_sp': expected_sp
        })
    else:
        return jsonify({'error': 'Location not found'})


if __name__ == '__main__':
    app.run(debug=True)
