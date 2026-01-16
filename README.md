**HomeWorth: House Price Prediction System using Linear Regression
Project Overview**

HomeWorth is a machine learning–based web application developed to predict residential property prices based on essential housing attributes. The system utilizes Linear Regression, a supervised learning algorithm, to estimate house prices by analyzing historical real estate data. The application provides an intuitive user interface built with Streamlit, allowing users to obtain real-time predictions by selecting property details.

This project demonstrates the practical implementation of machine learning concepts in the domain of real estate price prediction and serves as an academic project for undergraduate studies.

**Objectives**

- To design and implement a house price prediction system using machine learning.

- To apply Linear Regression for modeling the relationship between property features and price.

- To provide an interactive and user-friendly web interface for prediction.

- To understand feature engineering techniques such as one-hot encoding.

- To deploy a trained machine learning model for real-world use.

**Machine Learning Model
**
**Algorithm Used: Linear Regression
**
Linear Regression is used to predict continuous values by modeling the linear relationship between independent variables (total area, number of bedrooms, bathrooms, and location) and the dependent variable (house price). The model is trained on preprocessed housing data and serialized using Pickle for deployment.

**Dataset and Features
**
The dataset consists of real estate property records with the following features:

Total Area (in square feet)

Number of Bedrooms (BHK)

Number of Bathrooms

Location (One-Hot Encoded)

Price (Target Variable)

Categorical location data is transformed using One-Hot Encoding, resulting in multiple location-based feature columns. This ensures compatibility with machine learning algorithms.

**System Architecture
**
Data Collection

Data Preprocessing and Cleaning

Feature Engineering (One-Hot Encoding)

Model Training using Linear Regression

Model Serialization

Web Application Deployment using Streamlit

**Technology Stack
**
Programming Language: Python

Machine Learning: Scikit-learn

Data Processing: Pandas, NumPy

Web Framework: Streamlit

Model Storage: Pickle

Version Control: Git & GitHub

**Key Features
**
Predicts house prices in real time

Displays real location names instead of encoded values

Simple and aesthetic user interface

Accurate predictions based on trained ML model

Modular and well-structured code

**Conclusion**

The HomeWorth system successfully demonstrates how machine learning can be applied to real-world real estate price prediction problems. By integrating data preprocessing, Linear Regression modeling, and a web-based interface, the project provides a complete end-to-end machine learning solution suitable for academic and practical learning purposes.
