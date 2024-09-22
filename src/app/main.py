import os
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'Welcome to LucyFuel 5D Revolution!'
if __name__ == '__main__':
    app.run(debug=True)