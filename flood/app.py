from flask import Flask, render_template, request
import numpy as np
import joblib

# ==========================================
# Initialize Flask App
# ==========================================

app = Flask(__name__)

# ==========================================
# Load Saved Model and Scaler
# ==========================================

model = joblib.load("floods.save")
scaler = joblib.load("transform.save")

# ==========================================
# Home Page
# ==========================================

@app.route("/")
def home():
    return render_template("home.html")


# ==========================================
# Prediction Page
# ==========================================

@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "GET":
        return render_template("index.html")

    try:

        temp = float(request.form["Temp"])
        humidity = float(request.form["Humidity"])
        cloud = float(request.form["Cloud Cover"])
        annual = float(request.form["ANNUAL"])
        janfeb = float(request.form["Jan-Feb"])
        marmay = float(request.form["Mar-May"])
        junsep = float(request.form["Jun-Sep"])
        octdec = float(request.form["Oct-Dec"])
        avgjune = float(request.form["avgjune"])
        sub = float(request.form["sub"])

        features = np.array([[
            temp,
            humidity,
            cloud,
            annual,
            janfeb,
            marmay,
            junsep,
            octdec,
            avgjune,
            sub
        ]])

        # Scale Input
        features = scaler.transform(features)

        # Prediction
        prediction = model.predict(features)

        if prediction[0] == 1:
            return render_template("chance.html")

        else:
            return render_template("no_chance.html")

    except Exception as e:
        return f"<h2>Error : {e}</h2>"


# ==========================================
# Run Application
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)