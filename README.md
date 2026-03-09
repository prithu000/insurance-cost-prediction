# Insurance Cost Prediction & BMI Calculator (Flask + Machine Learning)

A simple **Machine Learning web application** built with **Flask** that predicts medical insurance cost based on user inputs.
The project also includes an additional **BMI Calculator tool** to help users understand their health metrics.

---

## 🚀 Features

* Predict **medical insurance cost** using a trained ML model
* Built using **Flask backend**
* Clean **HTML + CSS frontend**
* **BMI Calculator** integrated in the same web app
* Input validation and error handling
* Dynamic prediction results
* Simple and responsive UI

---

## 🧠 Machine Learning Model

The insurance cost prediction model uses the following features:

* Age
* BMI
* Number of children
* Smoking status
* Gender

The model was trained using the **Insurance dataset** and saved using **Pickle**.

---

## 🛠️ Tech Stack

* Python
* Flask
* Scikit-learn
* Pandas
* HTML
* CSS
* Git & GitHub

---

## 📂 Project Structure

```
insurance-cost-prediction
│
├── app.py
├── models
│   ├── model.pkl
│   └── columns.pkl
│
├── static
│   └── style.css
│
├── templates
│   ├── index.html
│   └── bmi.html
│
├── data
│   └── insurance.csv
│
└── README.md
```

---

## ⚙️ Installation & Setup

Clone the repository:

```
git clone https://github.com/prithu000/insurance-cost-prediction.git
```

Go to the project folder:

```
cd insurance-cost-prediction
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the Flask application:

```
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 📊 BMI Categories

| BMI Range   | Category    |
| ----------- | ----------- |
| < 18.5      | Underweight |
| 18.5 – 24.9 | Normal      |
| 25 – 29.9   | Overweight  |
| ≥ 30        | Obese       |

---

## 💡 Future Improvements

* Deploy the project on **Render / Railway / AWS**
* Add **user authentication**
* Improve UI with **JavaScript animations**
* Store prediction history in a database
* Convert into a **REST API**

---

## 👨‍💻 Author

**Prithu Maheshwari**

If you like this project, feel free to ⭐ the repository.
