import pandas as pd
from sklearn.tree import DecisionTreeRegressor


def modeltrain(df):
	df_loan_status = df[[' loan_status']]
	df_cibil_score = df[[' cibil_score']]
	tree_model = DecisionTreeRegressor()
	tree_model.fit(df_cibil_score,df_loan_status)
	return tree_model


def preprocess(df):

	custom_mapping = {' Yes':1,' No':0}
	df[' self_employed'] = df[' self_employed'].map(custom_mapping)
	custom_mapping = {' Not Graduate':0,' Graduate':1}
	df[' education'] = df[' education'].map(custom_mapping)
	custom_mapping = {' Approved':1,' Rejected':0}
	df[' loan_status'] = df[' loan_status'].map(custom_mapping)
	return df

def main_function():
	df = pd.read_csv("loan_approval_dataset.csv")
	df = preprocess(df)
	model = modeltrain(df)
	return model