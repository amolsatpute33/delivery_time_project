from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    product_category = request.form["product_category"]
    warehouse = request.form["warehouse"]
    shipment_mode = request.form["shipment_mode"]
    weight = float(request.form["weight"])
    demand = float(request.form["demand"])
    cost = float(request.form["cost"])

    data = pd.DataFrame({
        "Product_Category":[product_category],
        "Warehouse_Location":[warehouse],
        "Product_Weight_kg":[weight],
        "Shipment_Mode":[shipment_mode],
        "Demand_forecast_units":[demand],
        "Shipping_Cost":[cost]
    })

    prediction = model.predict(data)

    return render_template(
        "result.html",
        prediction=round(prediction[0],2)

    )

if __name__ == "__main__":
    app.run(debug=True)
    
