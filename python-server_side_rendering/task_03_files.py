from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    with open('products.json') as f:
        return json.load(f)

def read_csv():
    with open('products.csv') as f:
        reader = csv.DictReader(f)
        return list(reader)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    
    data = read_json() if source == 'json' else read_csv()
    
    if product_id:
        product = next((p for p in data if str(p['id']) == product_id), None)
        if not product:
            return render_template('product_display.html', error="Product not found")
        data = [product]
    
    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
