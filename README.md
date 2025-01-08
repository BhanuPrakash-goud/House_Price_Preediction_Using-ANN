# House_Price_Preediction_Using-ANN

## **Project Overview**
The House Price Prediction project is a machine learning application that leverages **Artificial Neural Networks (ANNs)** to predict house prices based on key features such as location, size, and amenities. This tool is designed to assist buyers, sellers, and real estate professionals by providing accurate and reliable price estimations.

---

## **Features**
- **Predictive Model**: Provides precise house price predictions using advanced ANN techniques.
- **Comprehensive Data Analysis**: Includes data preprocessing, feature scaling, and exploratory data analysis to ensure data quality.
- **Scalable and Customizable**: Adaptable to different datasets and regions, catering to a wide range of real estate markets.

---

## **Technical Stack**
- **Programming Language**: Python
- **Libraries Used**:
  - Flask
  - TensorFlow
  - NumPy
  - Pandas
  - Scikit-learn
  - Matplotlib
- **Machine Learning Model**: Artificial Neural Network (ANN)
- **Data**: Historical housing data with features such as area, number of rooms, location, and property type.

---

## **Project Workflow**

### **1. Data Collection and Preprocessing**
- Gathered historical housing data.
- Cleaned and preprocessed data by handling missing values and outliers.
- Scaled numerical features using `StandardScaler`.
- Encoded categorical features using `OneHotEncoder`.

### **2. Model Design and Training**
- Built a multi-layer ANN using TensorFlow and Keras.
- Split data into training, validation, and testing sets.
- Trained the ANN with optimal hyperparameters to ensure high accuracy.

### **3. Model Evaluation**
- Evaluated the model using metrics such as:
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)
- Optimized the model through hyperparameter tuning.

### **4. Deployment**
- Integrated the trained ANN model into a Flask web application.
- Users can input property details, and the app predicts house prices in real-time.

---

## **How to Run the Project**

### **1. Clone the Repository**
```bash
git clone <repository-url>
cd house-price-prediction
```

### **2. Install Dependencies**
Create a `requirements.txt` file with the following content:
```plaintext
Flask
numpy
pandas
tensorflow
scikit-learn
```
Then run:
```bash
pip install -r requirements.txt
```

### **3. Run the Flask Application**
```bash
python app.py
```

### **4. Access the Application**
Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

---

## **Usage**
1. Input property details (e.g., area, location, number of rooms, etc.) into the web application.
2. Submit the form to get the predicted house price.

---

## **Future Scope**
- **Enhanced Feature Set**: Incorporate additional features like market trends and proximity to amenities.
- **Global Dataset Support**: Expand support for datasets from various countries.
- **Visualization**: Add graphical insights for data and predictions.

---

## **Contributors**
- **Bhanu Prakash**

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Acknowledgments**
- Inspired by real-world challenges in the real estate market.
- Special thanks to the open-source community for providing resources and tools.

