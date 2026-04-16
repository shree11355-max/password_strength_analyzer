import string
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#  Logic-based "AI" model
def password_strength(features):
    length, uppercase, digits, special = features

    score = 0

    if length >= 8:
        score += 1
    if uppercase > 0:
        score += 1
    if digits > 0:
        score += 1
    if special > 0:
        score += 1

    if score <= 1:
        return "Weak"
    elif score <= 3:
        return "Medium"
    else:
        return "Strong"


# 🔍 Feature extraction
def extract_features(password):
    length = len(password)
    uppercase = sum(1 for c in password if c.isupper())
    digits = sum(1 for c in password if c.isdigit())
    special = sum(1 for c in password if c in string.punctuation)

    return [length, uppercase, digits, special]


# 🏠 Home route
@app.route("/")
def home():
    return "Password Strength API Running 🚀"


# 🔮 Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "password" not in data:
        return jsonify({"error": "Password required"}), 400

    password = data["password"]

    features = extract_features(password)
    strength = password_strength(features)

    return jsonify({
        "password": password,
        "strength": strength,
        "features": {
            "length": features[0],
            "uppercase": features[1],
            "digits": features[2],
            "special": features[3]
        }
    })


#  Run server on PORT 8000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)