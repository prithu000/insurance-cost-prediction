from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("models/model.pkl", "rb"))
columns = pickle.load(open("models/columns.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    try:
        age = int(request.form["age"])
        bmi = float(request.form["bmi"])
        children = int(request.form["children"])
        smoker = int(request.form["smoker"])
        gender = int(request.form["gender"])

        import pandas as pd

        input_data = {
            "age": age,
            "bmi": bmi,
            "children": children,
            "sex_male": gender,
            "smoker_yes": smoker
        }

        df = pd.DataFrame([input_data])
        df = df.reindex(columns=columns, fill_value=0)

        prediction = model.predict(df)[0]

        return render_template(
            "index.html",
            prediction_text=f"Predicted Insurance Cost : $ {round(prediction,2)}"
        )

    except Exception as e:

        return render_template(
            "index.html",
            prediction_text=f"INVALID INPUT"
        )

@app.route("/bmii")
def bmi():
    return render_template("bmi.html")

@app.route("/bmi", methods=["POST"])
def calculate_bmi():
    try:
        weight = float(request.form["weight"])
        height = float(request.form["height"])

        bmi = weight / (height ** 2)

        return render_template(
            "bmi.html",
            bmi_text=f"Calculated BMI : {round(bmi,2)}",
            bmi=bmi
        )

    except :
        return render_template(
            "index.html", bmi=bmi,
            bmi_text=f"INVALID INPUT"
        )

    
if __name__ == "__main__":
    app.run(debug=True)