import os
from flask import Flask

app = Flask(__name__)
port = int(os.environ.get('PORT', 3000))

@app.route('/')
def hello():
    return "Hello from my first Python app on SAP BTP - version 2!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
