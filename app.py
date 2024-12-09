from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Import CORS
from chat import get_response

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/")
def index_get():
    return render_template("base.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
