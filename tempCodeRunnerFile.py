import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load the dataset
dataset_path = 'C:\dataset\Hyderabad.csv'
data = pd.read_csv(dataset_path)

# Assuming 'price' is the target column
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

# Split the data into training and testing sets
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

# Function to preprocess user input
def preprocess_user_input(user_input):
    user_input_df = pd.DataFrame(user_input, index=[0])
    user_input_preprocessed = preprocessor.transform(user_input_df).toarray()
    return user_input_preprocessed

# Function to predict house price based on preprocessed user input
def predict_house_price(preprocessed_input):
    # Make predictions
    predicted_price = model.predict(preprocessed_input)[0, 0]
    return predicted_price

# Take inputs from the user
user_input = {}
for column in features.columns:
    user_input[column] = input(f"Enter value for {column}: ")

# Preprocess user input
user_input_preprocessed = preprocess_user_input(user_input)

# Predict house price based on preprocessed user input
predicted_price = predict_house_price(user_input_preprocessed)
print(f'Predicted Price: {predicted_price}')