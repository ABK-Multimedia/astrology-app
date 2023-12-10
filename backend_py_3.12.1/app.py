from flask import Flask

app = Flask(__name__)

@app.route('/api/data')

def get_data():
    return {'message': 'Hello from Python backend!'}

if __name__ == '__main__':
    app.run(host='localhost', port=5020, debug=True)
