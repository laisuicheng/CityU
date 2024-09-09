# %%
import pandas as pd
import numpy as np
import joblib
# from flaml import AutoML
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# %%
# Load the datasets
df1 = pd.read_csv('./kaggle/input/restaurant-data-with-consumer-ratings/rating_final.csv')
df2 = pd.read_csv('./kaggle/input/restaurant-data-with-consumer-ratings/userprofile.csv')
df3 = pd.read_csv('./kaggle/input/restaurant-data-with-consumer-ratings/geoplaces2.csv')

# Merge the datasets on the common column 'userID'
df = pd.merge(df1, df2, on='userID')
df = pd.merge(df, df3, on='placeID')

# Explore the merged dataset
# print(df.head())
# print(df.info())
# print(df.describe())


# %%
# Drop insensitive features
df = df.drop('latitude_x', axis=1)  
df = df.drop('longitude_x', axis=1)  
df = df.drop('latitude_y', axis=1)  
df = df.drop('longitude_y', axis=1)  
df = df.drop('food_rating', axis=1)  
df = df.drop('service_rating', axis=1)  
df = df.drop('birth_year', axis=1)  
df = df.drop('weight', axis=1)  
df = df.drop('height', axis=1)
df = df.drop('url', axis=1)
df = df.drop('the_geom_meter', axis=1)
df = df.drop('placeID', axis=1)
df = df.drop('userID', axis=1)
df = df.drop('address', axis=1)
df = df.drop('city', axis=1)
df = df.drop('state', axis=1)
df = df.drop('fax', axis=1)
df = df.drop('zip', axis=1)
df = df.drop('other_services', axis=1)


# Handle missing values if any
df = df.dropna()

# Convert categorical variables to numerical (if any)
df = pd.get_dummies(df, drop_first=True)

# Split the data into features and target
X = df.drop('rating', axis=1)  # Replace 'target_column' with the actual target column name
y = df['rating']

# print(X.head())
# print(X.info())
# print(X.describe())
# print(y.head())

# print(X.isnull().sum())
# print(y.isnull().sum())


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# %%
# Train the model using specific algorithms
# model = LogisticRegression()
model = RandomForestClassifier(n_estimators=1000)
model.fit(X_train, y_train)

# Train the model using AutoML
# model = AutoML()
# model.fit(X_train=X, y_train=y, task="classification", time_budget=90)


# Save the model
joblib.dump(model, "./restaurant_recommendation_model.joblib")



# Make predictions
# y_pred = model.predict(X_test)
y_pred = model.predict(X_test)

# Evaluate the model
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print('Confusion Matrix:')
print(conf_matrix)
print('Classification Report:')
print(class_report)



import csv

# Write the first row of X_test into a CSV file
first_row = pd.DataFrame(X_test[0]).T
first_row.to_csv('first_row_X_test.csv', index=False)