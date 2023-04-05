from flask import Flask, render_template, request, flash, redirect, url_for
import secrets
import os

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    flash('Application has been successfuly run.')
    script_path = os.path.join(os.getcwd(), 'main.py')
    os.system(f'python {script_path}')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)