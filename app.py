from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import os

app = Flask(__name__)

# Load the dataset
dataset_path = r'C:\dataset\Hyderabad.csv'  # Using raw string literal

# Check if the file exists before loading
if os.path.exists(dataset_path):
    data = pd.read_csv(dataset_path)
else:
    raise FileNotFoundError(f"File '{dataset_path}' not found.")

# Assuming 'Price' is the target column
target = data['Price']
features = data.drop('Price', axis=1)

# Separate numerical and categorical columns
numerical_cols = features.select_dtypes(include=np.number).columns.tolist()
categorical_cols = features.select_dtypes(exclude=np.number).columns.tolist()

# Preprocessing pipeline for numerical features
numerical_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

# Preprocessing pipeline for categorical features
categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Combine numerical and categorical transformers
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

# Load the trained model
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Apply the preprocessing pipeline to the training set
X_train_preprocessed = preprocessor.fit_transform(X_train)

# Convert sparse matrix to dense array for training
X_train_preprocessed_dense = X_train_preprocessed.toarray()

# Build the neural network model with dropout
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(X_train_preprocessed_dense.shape[1],)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Early stopping callback
early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# Train the model with early stopping without printing loss
model.fit(X_train_preprocessed_dense, y_train, epochs=50, batch_size=32, validation_split=0.2, callbacks=[early_stopping], verbose=0)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.form.to_dict()
    user_input_preprocessed = preprocess_user_input(user_input)
    predicted_price = predict_house_price(user_input_preprocessed)
    formatted_price = format_predicted_price(predicted_price)
    return formatted_price

def preprocess_user_input(user_input):
    user_input_df = pd.DataFrame(user_input, index=[0])
    user_input_preprocessed = preprocessor.transform(user_input_df).toarray()
    return user_input_preprocessed

def predict_house_price(preprocessed_input):
    predicted_price = model.predict(preprocessed_input)[0, 0]
    return predicted_price*1.258

def format_predicted_price(predicted_price):
    formatted_price = f'₹ {predicted_price:.2f}'  # Format as Indian Rupees with two decimal places
    return formatted_price

if __name__ == '__main__':
    app.run(debug=True)
