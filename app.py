from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['get'])
def hello():
    return '<h1>hello_world</h1>'


@app.route('/api', methods=['post'])
def hellome():
    a=5
    b=5
    c = a+b
    return c

if __name__ == '__main__':
    app.run()
