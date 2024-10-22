from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample asset data (in-memory for simplicity)
assets = []

@app.route('/')
def index():
    return render_template('index.html', assets=assets)

@app.route('/add_asset', methods=['POST'])
def add_asset():
    asset_name = request.form['name']
    asset_type = request.form['type']
    asset_status = request.form['status']
    assets.append({'name': asset_name, 'type': asset_type, 'status': asset_status})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
