from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# 读取Excel文件
excel_file = 'data.xlsx'  # 替换为您的Excel文件路径
df = pd.read_excel(excel_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    location = request.form.get('location')
    if location in df.columns:
        data = df[location].to_dict()
        labels = list(data.keys())
        values = list(data.values())
        return jsonify({'labels': labels, 'values': values})
    else:
        return jsonify({'error': 'Location not found'})

if __name__ == '__main__':
    app.run(debug=True)
