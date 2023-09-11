from flask import Flask , render_template , request , make_response ,flash , redirect , url_for,jsonify
import pandas as pd
import logging
from cibil_model import main_function
from loan_amount import loan_model_init
import math

app =  Flask(__name__)

app.config['cibil_model'] = main_function()
app.config['loan_model'] = loan_model_init()

@app.route("/cibil_score/<int:cibil_value>")
def cibi_score(cibil_value):
	cibil_model = app.config['cibil_model']
	value = cibil_model.predict([[cibil_value]])
	grant = False
	if value[0] == 1:
		grant = True
	return jsonify({'result':grant})
	

@app.route("/details/<string:values>")
def loan_amount(values):
	item_list = [int(value) for value in values.split(",")]
	loan_model = app.config['loan_model']
	res = loan_model.predict([item_list])
	#print(res[0][0],"******************")
	return jsonify({'result' : math.ceil(res[0][0])})


@app.route("/")
def home_route():
	return render_template("home.html")



if __name__ == '__main__':
   app.run(debug = True)