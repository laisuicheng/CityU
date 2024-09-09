import requests
import pandas as pd
import numpy as np
import json
from app import app
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Extract a sample from X_test
sample = X_test[0]  # You can choose any row, here we choose the first row

# Convert the sample to a dictionary
sample_dict = {f'feature_{i}': sample[i] for i in range(len(sample))}

# Convert the dictionary to JSON
sample_json = json.dumps(sample_dict, indent=4)
print(sample_json)

"""
# Post the JSON for prediction
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
        
def test_predict(client):
    data = sample_json
    # Wrap the data in a list to create a DataFrame with a single row
    response = client.post('/predict', 
                           data=json.dumps(data), 
                           content_type='application/json')
    assert response.status_code == 200
    assert isinstance(response.json, list)


if __name__ == '__main__':
    pytest.main()

"""


# Load test data from CSV file
test_data = pd.read_csv('first_row_X_test.csv')
# Convert test data to dictionary
test_data_dict = test_data.to_dict(orient='records')

test_data_json = test_data.to_json(orient='records')

# Post the JSON for prediction
url = 'http://127.0.0.1:5000/predict'
data = test_data_json
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)
print(response.text)  # Print the raw response text
try:
    print(response.json())
except requests.exceptions.JSONDecodeError:
    print("Response is not in JSON format")
