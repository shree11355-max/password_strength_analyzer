import pickle

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
    elif score == 2 or score == 3:
        return "Medium"
    else:
        return "Strong"

# Save function as "model"
with open("model/password_model.pkl", "wb") as f:
    pickle.dump(password_strength, f)

print("Model (logic-based) saved successfully")