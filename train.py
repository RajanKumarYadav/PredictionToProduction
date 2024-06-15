# Import necessary libraries
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Load the Iris dataset
df = pd.read_csv('diabetes.csv')
X = df.drop('Outcome',axis=1)
y = df['Outcome']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y , test_size=0.3, random_state=42)

# Create the classifier
logmodel = LogisticRegression()

# Train the classifier
logmodel.fit(X_train,y_train)
print('Training completed')
print("Save model")

# saving our model # model - model , filename-model_jlib
joblib.dump(logmodel , 'log_model_diabetes_prediction') # Can be Any Cloud Location # Can be Any Model Regstry