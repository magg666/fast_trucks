from flask import Flask
from  app import path_to_target

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    data = path_to_target
    return data


if __name__ == '__main__':
    app.run()
