from flask import Flask

app = Flask(__name__)


# decorador e rota a ser invocada.
@app.route("/", methods=['GET', 'POST'])
def api():
    return 'estrutura base api'


if __name__ == "__main__":
    app.run(debug=True)
