# 🛒 Customer Purchase Prediction

A Machine Learning project that predicts whether an online shopper is likely to make a purchase based on their browsing behavior and session information.

The project uses a **Random Forest Classifier** with a Scikit-learn Pipeline and provides an interactive web application built with Streamlit.

## 🚀 Live Demo

[Try the Customer Purchase Prediction App](https://customer-purchase-prediction-yz4c.onrender.com)

## 📌 Project Overview

The goal of this project is to predict customer purchasing intentions using the Online Shoppers Purchasing Intention Dataset.

The model analyzes customer session data and predicts whether a visitor is likely to complete a purchase.

## 🧠 Machine Learning

- **Problem Type:** Binary Classification
- **Algorithm:** Random Forest Classifier
- **Preprocessing:** Scikit-learn Pipeline
- **Model Evaluation:** Precision, Recall, F1-Score, Accuracy
- **Model Saving:** Joblib

## 📊 Model Performance

The model achieved the following results on the test dataset:

| Metric | Score |
|---|---:|
| Accuracy | 89% |
| Precision (Purchase) | 61% |
| Recall (Purchase) | 72% |
| F1-Score (Purchase) | 66% |

The model achieves good overall accuracy while identifying a reasonable proportion of customers who are likely to make a purchase.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

## 📂 Project Structure

```text
Customer-Purchase-Prediction/
│
├── app.py
├── costumer_purchase.ipynb
├── online_shoppers_intention.csv
├── purchase_model_compressed.joblib
├── requirements.txt
└── .python-version
```

## ⚙️ Installation & Usage

1. Clone the repository:

```bash
git clone https://github.com/amir13895/Customer-Purchase-Prediction.git
```

2. Navigate to the project directory:

```bash
cd Customer-Purchase-Prediction
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit application:

```bash
streamlit run app.py
```

## 🌐 Deployment

The application is deployed using **Render** and is accessible online.

[Live Application](https://customer-purchase-prediction-yz4c.onrender.com)

## 🎯 Project Goals

- Apply Machine Learning concepts to a real-world problem.
- Build a classification model using Scikit-learn.
- Implement data preprocessing with Pipelines.
- Evaluate model performance.
- Deploy a Machine Learning application using Streamlit.

## 👨‍💻 Author

**Amirreza Sedghi**

Aspiring AI & Machine Learning Developer

Interested in Python, Artificial Intelligence, Machine Learning, and practical AI applications.

GitHub: [@amir13895](https://github.com/amir13895)

---

*This project was developed for educational purposes and practical Machine Learning experience.*
