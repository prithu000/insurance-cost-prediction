# Insurance Cost Prediction System

A simple machine learning web application that predicts medical insurance costs based on user information.
The model is trained using the **Medical Cost Personal Dataset** and deployed with **Flask**.

This project demonstrates a complete machine learning workflow — from data preprocessing and model training to deploying the model through a web interface.

---

## Project Overview

Insurance companies estimate medical costs using various personal and health-related factors.
This application allows users to input their details and receive an estimated insurance cost prediction.

The prediction is generated using a **Linear Regression model trained with Scikit-Learn**.

---

## Features

* Predict insurance cost based on:

  * Age
  * BMI (Body Mass Index)
  * Number of children
  * Gender
  * Smoker status

* Simple web interface built with Flask

* Machine learning model built using Scikit-Learn

* Clean dark-themed UI with custom CSS

* End-to-end ML pipeline demonstration

---

## Tech Stack

**Backend**

* Python
* Flask

**Machine Learning**

* Scikit-Learn
* Pandas
* NumPy

**Frontend**

* HTML
* CSS

---

## Project Structure

```
insurance-cost-prediction
│
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
│
├── data
│   └── insurance.csv      # Dataset used for training
│
├── models
│   └── model.pkl          # Trained ML model
│
├── templates
│   └── index.html         # Web interface
│
└── static
    └── style.css          # Custom styling
```

---

## Machine Learning Workflow

1. Load dataset
2. Perform preprocessing and encoding
3. Train Linear Regression model
4. Evaluate model performance
5. Save trained model using Pickle
6. Deploy model using Flask
7. Accept user input from web interface
8. Generate prediction

---

## Dataset

The model is trained using the **Medical Cost Personal Dataset**, which contains information about:

* Age
* Gender
* BMI
* Children
* Smoker status
* Region
* Insurance charges

Target variable:

```
charges
```

The model learns the relationship between these features and insurance cost.

---

## How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/prithu0000/insurance-cost-prediction.git
```

### 2. Navigate to the project folder

```
cd insurance-cost-prediction
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the Flask application

```
python app.py
```

### 5. Open the application

```
http://127.0.0.1:5000
```

---

## Example Input

User enters:

* Age: 35
* BMI: 28
* Children: 2
* Gender: Male
* Smoker: Yes

The model returns a predicted insurance cost.

---

## Future Improvements

Possible improvements for the project:

* Use advanced models (Random Forest / Gradient Boosting)
* Add input validation
* Add visual analytics dashboard
* Deploy the application online
* Implement a full ML pipeline using Scikit-Learn Pipeline

---

## Author

**Prithu Maheshwari**

BTech Computer Science Engineering student interested in
Machine Learning, Data Science, and Backend Development.

---
