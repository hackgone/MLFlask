from sklearn.linear_model import Ridge
import pandas as pd


def model_train(df):
	ridge_model = Ridge(alpha=0.1)
	corr_matrix = df.corr()
	list1 = corr_matrix[" loan_amount"].sort_values(ascending=False)
	list_x = []
	for key,value in list1.items():
		if(key!=" loan_amount" and value>=0.5):
			list_x.append(key)
	df_independent = df[list_x]
	df_dependent = df[[' loan_amount']]
	ridge_model.fit(df_independent,df_dependent)
	return ridge_model

def preprocess(df):
	custom_mapping = {' Yes':1,' No':0}
	df[' self_employed'] = df[' self_employed'].map(custom_mapping)
	custom_mapping = {' Not Graduate':0,' Graduate':1}
	df[' education'] = df[' education'].map(custom_mapping)
	custom_mapping = {' Approved':1,' Rejected':0}
	df[' loan_status'] = df[' loan_status'].map(custom_mapping)
	return df



def loan_model_init():
	
    df = pd.read_csv("loan_approval_dataset.csv")
    df = preprocess(df)
    ridge_model = model_train(df)
    return ridge_model

        
	
        
