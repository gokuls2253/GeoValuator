import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Set BASE_DIR to the root of your Django project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dataset_path = os.path.join(BASE_DIR, 'housing/ml_model/Bengaluru_House_Data.csv')

# Load the dataset
df = pd.read_csv(dataset_path)

# Extract the location name before the first comma
df['location'] = df['location'].apply(lambda x: x.split(',')[0])

# Clean the data by converting columns to numeric and removing invalid entries
df['total_sqft'] = pd.to_numeric(df['total_sqft'], errors='coerce')
df['size'] = pd.to_numeric(df['size'], errors='coerce')
df['bath'] = pd.to_numeric(df['bath'], errors='coerce')
df['balcony'] = pd.to_numeric(df['balcony'], errors='coerce')
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Drop rows with any NaN values
df = df.dropna()

# Preprocess the dataset for model input
X = df[['total_sqft', 'size', 'bath', 'balcony']]  # Features for prediction
y = df['price']  # Target variable (house price)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model as a pickle file
model_path = os.path.join(BASE_DIR, 'housing/ml_model/house_price_model.pkl')
with open(model_path, 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved as pickle at:", model_path)
