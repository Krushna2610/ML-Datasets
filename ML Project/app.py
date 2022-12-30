from flask import Flask,render_template,request
import pickle
import sklearn
import numpy as np

app=Flask(__name__)
model=pickle.load(open("rf_model.pkl","rb"))

@app.route("/")
def home_func():
    return render_template("home.html")


@app.route("/predict",methods=['POST'])
def predict():
    if request.method=='POST':
        year=int(request.form['year'])
        present_price=float(request.form['price'])
        km_driven=int(request.form['km_driven'])
        owner=int(request.form['owner'])
        fuel_type_petrol=request.form['Fuel_Type']
        if (fuel_type_petrol=='petrol'):
            fuel_type_petrol=1
            fuel_type_diesel=0
        else:
            fuel_type_petrol=1
            fuel_type_diesel=0
            seller_type_individual=request.form['seller_type']
        if seller_type_individual=='Individual':
            seller_type_individual=1
        else:
            seller_type_individual=0
        transmission_manual=request.form['transmission_type']
        if transmission_manual=='Manual':
            transmission_manual=1
        else:
            transmission_manual=0
        prediction=model.predict([[present_price,km_driven,owner,year,fuel_type_diesel,fuel_type_petrol,seller_type_individual,transmission_manual]])
        output=prediction[0]

        if output:
            return render_template("home.html",prediction_text="Sorry you cannot sell this car")
        else:
            return render_template("home.html",prediction_text="you can sell the car at {}".format(output))
    else:
        return render_template("home.html")









if __name__=="__main__":
    app.run(debug=True)