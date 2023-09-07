from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the dataset using pandas
df = pd.read_excel('data.xlsx', index_col=0)

@app.route('/', methods=['GET', 'POST'])
def index():
    categories, values, average_values = [], [], []

    if request.method == 'POST':
        location = request.form.get('query').strip().lower()

        if location in df.index:
            categories = list(df.columns)
            values = df.loc[location].tolist()
            average_values = df.mean().tolist()

    return render_template('index.html', categories=categories, values=values, average_values=average_values)

if __name__ == '__main__':
    app.run(debug=True)
