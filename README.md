# Fraud Detection using Machine Learning

## 📌 Project Overview

This project is a **Machine Learning-based Fraud Detection system** that predicts whether a financial transaction is likely to be fraudulent or not.
## 🚀 Live Demo

👉 [Click here to open the Fraud Detection App]
  (Local URL: http://localhost:8501
  Network URL: http://192.168.1.6:8501)

The project includes:

- Exploratory Data Analysis (EDA)
- Data preprocessing
- Feature engineering
- Handling imbalanced classes
- Logistic Regression model
- Model evaluation
- Saving the trained ML pipeline using Joblib
- A Streamlit web application for making predictions

---

## 🎯 Objective

The main objective of this project is to build a machine learning model that can identify potentially fraudulent transactions based on transaction details such as:

- Transaction type
- Transaction amount
- Sender's old balance
- Sender's new balance
- Receiver's old balance
- Receiver's new balance

The model predicts:

```text
0 → Not Fraud
1 → Fraud
```

---

## 📊 Exploratory Data Analysis

The dataset was explored to understand the transaction patterns and identify characteristics associated with fraudulent transactions.

The analysis included:

- Checking dataset shape and columns
- Checking missing values
- Analyzing fraud vs non-fraud transactions
- Analyzing transaction types
- Analyzing fraud rate by transaction type
- Analyzing transaction amount distribution
- Comparing transaction amounts for fraud and non-fraud transactions
- Analyzing fraud occurrences over time
- Identifying frequently occurring senders and receivers
- Examining fraud-related users
- Analyzing correlations between numerical variables

Visualizations were created using **Matplotlib and Seaborn**.

---

## 🛠️ Feature Engineering

Additional features were created from the existing balance information.

### Balance Difference for Sender

```text
balanceDiffOrig = oldbalanceOrg - newbalanceOrig
```

This represents the change in the sender's balance.

### Balance Difference for Receiver

```text
balanceDiffDest = newbalanceDest - oldbalanceDest
```

This represents the change in the receiver's balance.

These features help provide additional information about how balances change during a transaction.

---

## 🤖 Machine Learning

### Algorithm Used

**Logistic Regression**

Logistic Regression was used as a binary classification algorithm to predict whether a transaction is fraudulent.

```text
0 → Not Fraud
1 → Fraud
```

### Input Features

The model uses:

- `type`
- `amount`
- `oldbalanceOrg`
- `newbalanceOrig`
- `oldbalanceDest`
- `newbalanceDest`

---

## 🔄 Data Preprocessing

A Scikit-learn `ColumnTransformer` was used to apply different preprocessing techniques to numerical and categorical features.

### Numerical Features

The numerical features were standardized using:

```text
StandardScaler
```

### Categorical Features

The transaction type was converted into numerical form using:

```text
OneHotEncoder
```

with:

```text
drop="first"
```

---

## ⚖️ Handling Class Imbalance

Fraudulent transactions are much less common than normal transactions.

To give more importance to the minority class, Logistic Regression was configured with:

```python
class_weight="balanced"
```

This helps the model pay more attention to fraudulent transactions during training.

---

## 🔗 Machine Learning Pipeline

A Scikit-learn Pipeline was created to combine preprocessing and model training.

The workflow is:

```text
Raw Transaction Data
        ↓
ColumnTransformer
        ↓
Numerical → StandardScaler
Categorical → OneHotEncoder
        ↓
Logistic Regression
        ↓
Fraud Prediction
```

This ensures that the same preprocessing steps are applied when making predictions on new data.

---

## 📈 Model Evaluation

The model was evaluated using:

- Classification Report
- Confusion Matrix
- Accuracy

The classification report provides:

- Precision
- Recall
- F1-score
- Support

The confusion matrix helps identify:

- True Positives
- True Negatives
- False Positives
- False Negatives

For fraud detection, precision and recall are particularly useful because the dataset contains an imbalance between fraudulent and normal transactions.

---

## 💾 Saving the Model

The complete preprocessing and Logistic Regression pipeline was saved using Joblib:

```python
joblib.dump(pipeline, "fraud_detection_pipeline.pkl")
```

This allows the trained pipeline to be reused without training the model again.

---

## 🌐 Streamlit Web Application

A Streamlit application was created to allow users to enter transaction details and receive a fraud prediction.

The application accepts:

- Transaction type
- Transaction amount
- Sender's old balance
- Sender's new balance
- Receiver's old balance
- Receiver's new balance

The user clicks the **Predict** button and the trained model returns:

```text
0 → Not Fraud
1 → Fraud
```

The application then displays an appropriate message.

---

## 📁 Project Structure

```text
Fraud-Detection/
│
├── AIML dataset.csv
├── analysis_model.ipynb
├── fraud_detection.py
├── fraud_detection_pipeline.pkl
└── README.md
```

> File names can be adjusted according to the actual files uploaded to the repository.

---

## 🧰 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project directory

```bash
cd Fraud-Detection
```

### 3. Install the required libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib streamlit
```

### 4. Run the Streamlit application

```bash
streamlit run fraud_detection.py
```

The Streamlit application will open in your browser.

---

## 🔮 Future Improvements

Some possible improvements include:

- Experimenting with additional classification algorithms
- Hyperparameter tuning
- Using additional engineered features
- Comparing multiple evaluation metrics
- Improving fraud detection recall
- Adding probability-based predictions
- Deploying the Streamlit application online

---

## 👩‍💻 Author

**Koel Saha**

Machine Learning / Data Science Project
