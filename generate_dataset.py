import random
import string
import pandas as pd

def generate_password(length):
    "l""Create a random password of given length."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def extract_features(password):
    """Turn a password into 4 numbers (features for ML)."""
    length        = len(password)
    uppercase     = sum(1 for c in password if c.isupper())
    digits        = sum(1 for c in password if c.isdigit())
    special_chars = sum(1 for c in password if c in string.punctuation)
    return length, uppercase, digits, special_chars

def label_password(length, uppercase, digits, special_chars):
    """Rule-based label — this is what the ML model will learn to copy."""
    score = 0
    if length >= 12: score += 2
    elif length >= 8: score += 1
    if uppercase >= 2: score += 1
    if digits >= 2:    score += 1
    if special_chars >= 2: score += 2
    elif special_chars >= 1: score += 1

    if score >= 5: return "Strong"
    elif score >= 3: return "Medium"
    else:           return "Weak"

# Generate 200 sample passwords
data = []
for _ in range(200):
    length   = random.randint(4, 20)
    password = generate_password(length)
    l, u, d, s = extract_features(password)
    label    = label_password(l, u, d, s)
    data.append([l, u, d, s, label])

df = pd.DataFrame(data, columns=["length", "uppercase", "digits", "special", "label"])
df.to_csv("dataset/passwords.csv", index=False)
print("Dataset saved! Shape:", df.shape)
print(df["label"].value_counts())  # see how many Weak/Medium/Strong