from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Ahoj Světe! Jak to de?"

if __name__ == "__main__":
    application.run()
