from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json():
    with open('products.json') as f:
        return json.load(f)

def read_csv():
    with open('products.csv') as f:
        reader = csv.DictReader(f)
        return list(reader)

def read_sql():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    conn.close()
    return results

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")
    
    try:
        if source == 'json':
            data = read_json()
        elif source == 'csv':
            data = read_csv()
        else:
            data = read_sql()
        
        if product_id:
            product = next((p for p in data if str(p['id']) == product_id), None)
            if not product:
                return render_template('product_display.html', error="Product not found")
            data = [product]
        
        return render_template('product_display.html', products=data)
    except Exception as e:
        return render_template('product_display.html', error=f"An error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
