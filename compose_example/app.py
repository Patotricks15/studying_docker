from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Olá, mundo! Esse é um app simples com Docker Compose."

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
