from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

excel_file = 'data.xlsx'  #Data input

df = pd.read_excel(excel_file)

@app.route('/')
def index():
    return render_template('index2.html')

def avg(column):
    return sum(column) / len(column)


def ratio(df):
    return avg(df.loc['gp']), avg(df.loc['ep']), avg(df.loc['specialist'])


def prediction(population, growth, ratio):
    return round(population * (1 + growth) * ratio)

@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    location = request.form.get('location')
    if location in df.columns:
        data = df[location].to_dict()
        labels = list(data.keys())
        values = list(data.values())

        expected_gp =10  # Your logic for expected gp
        expected_ep = 11  # Your logic for expected ep
        expected_sp = 12
        return jsonify({
            'labels': labels, 
            'values': values,
            'expected_gp': expected_gp,
            'expected_ep': expected_ep,
            'expected_sp': expected_sp
        })
        #return jsonify({'labels': labels, 'values': values})
    else:
        return jsonify({'error': 'Location not found'})

if __name__ == '__main__':
    app.run(debug=True)
