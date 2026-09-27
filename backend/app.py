from flask import Flask

from routes.prediction import prediction_bp


app = Flask(__name__)


# Register prediction API
app.register_blueprint(
    prediction_bp
)


@app.route("/")
def home():

    return "Skin Screening API is running!"


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )