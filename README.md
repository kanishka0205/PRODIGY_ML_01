# 🏡 House Price Prediction using Linear Regression

This project implements a simple **Linear Regression** model to predict house prices based on key features like **square footage**, **number of bedrooms**, and **number of bathrooms**. The aim is to explore how these factors influence house pricing and apply machine learning techniques to build an accurate prediction model.

## 📌 Project Objective

To build a machine learning model using **Linear Regression** that can:

- Predict the price of a house.
- Understand the relationship between the price and features like:
  - Square footage
  - Number of bedrooms
  - Number of bathrooms

---

## 📁 Dataset

The dataset contains the following columns:

- SquareFootage — Total area of the house in square feet
- Bedrooms — Number of bedrooms
- Bathrooms — Number of bathrooms
- Price — Price of the house (target variable)

dataset:- https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data

---

## 🛠️ Technologies Used

- Python 🐍
- Pandas 📊
- NumPy 🔢
- Matplotlib & Seaborn 📈
- Scikit-learn 🤖
- Jupyter Notebook 📒

---

## 🔍 Exploratory Data Analysis (EDA)

Before modeling, the data is cleaned and analyzed:

- Checked for missing values
- Visualized feature distributions
- Explored correlations between features and the target variable
- Handled outliers (if any)

---

## 🚀 Model Building Steps

1. **Data Preprocessing**
   - Clean and format the dataset
   - Normalize/standardize data (if needed)

2. **Splitting the Dataset**
   - Train-test split using train_test_split()

3. **Training the Model**
   - Fit the Linear Regression model using scikit-learn

4. **Evaluation**
   - Evaluate model performance using metrics like:
     - Mean Squared Error (MSE)
     - R-squared Score

---

## 📚 Learning Outcomes

- Applied Linear Regression on real-world-style data
- Practiced data cleaning, EDA, and modeling
- Learned to evaluate and interpret regression model results

---

## 💡 Future Work

- Include more features like location, year built, etc.
- Try other regression algorithms (Ridge, Lasso, Decision Tree)
- Improve model performance with feature engineering
