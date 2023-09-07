from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the dataset using pandas
df = pd.read_excel('data.xlsx', index_col=0)

@app.route('/', methods=['GET', 'POST'])
def index():
    data, query, average = {}, "", 0
    
    if request.method == 'POST':
        query = request.form.get('query')
        
        if query in df.columns:
            data = df[query].to_dict()
            average = df.mean(axis=1).to_dict()
    
    return render_template('index.html', data=data, query=query, average=average)

if __name__ == '__main__':
    app.run(debug=True)
