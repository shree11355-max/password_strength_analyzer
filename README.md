# 🔐 Password Strength Analyzer

## 👨‍💻 Team Members

* **Shree** (25215052)
* **Pratiksha** (25215044)
* **Tejashvi** (25215065)
* **Priya** (25215064)

---

## 📌 Project Overview

The **Password Strength Analyzer** is a simple AI-based web application that evaluates the strength of a password entered by the user.

It analyzes different characteristics of the password such as:

* Length
* Uppercase letters
* Digits
* Special characters

Based on these features, the system classifies the password as:
👉 **Weak / Medium / Strong**

---

## 🎯 Objective

The main objective of this project is to:

* Understand how password security works
* Build a basic AI-like system using feature extraction
* Implement a full-stack application (Frontend + Backend)
* Demonstrate API communication between client and server

---

## 🧠 Working Principle

1. User enters a password in the frontend
2. Frontend sends request to backend API
3. Backend extracts features:

   * Length
   * Uppercase count
   * Digits count
   * Special characters
4. A scoring logic is applied
5. Result is returned to frontend and displayed

---

## 🏗️ Tech Stack

### Frontend:

* HTML
* CSS
* JavaScript

### Backend:

* Python
* Flask
* Flask-CORS

---

## 📁 Project Structure

```
password-strength-analyzer/
│
├── backend/
│   └── app.py
│
├── frontend/
│   └── index.html
│
└── requirements.txt
```

---

## ⚙️ Installation & Setup


### 1. Install dependencies

```
brew install python3 (for mac setups)
py -0 (for windows)
check versions of python 

```

### 3. Run backend

```
cd backend
python3 app.py
```

---

## 🌐 Usage

1. Open the frontend (`index.html`) in browser
2. Enter a password
3. Click **Analyze**
4. View password strength result

---

## 🔍 Sample Inputs

| Password | Output |
| -------- | ------ |
| abc      | Weak   |
| abc123   | Medium |
| Abc@1234 | Strong |

---

## 🚀 Features

* Simple and clean UI
* Fast response time
* Real-time password analysis
* Backend API integration

---

## 📌 Future Improvements

* Add real Machine Learning model
* Strength meter visualization
* Password suggestions
* Deployment on cloud

---

## 📖 Conclusion

This project demonstrates how basic AI concepts like **feature extraction and decision-making logic** can be applied to real-world problems like password security.

It also showcases **end-to-end system development** including frontend, backend, and API integration.

---

## 📎 Note

This project is developed for academic purposes as part of AI coursework.