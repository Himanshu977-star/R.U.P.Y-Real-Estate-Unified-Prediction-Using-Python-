# Real Estate Price Prediction

## Overview
This project is a **Real Estate Price Prediction System** that uses **Machine Learning** to estimate home prices based on user inputs. It includes a **trained Linear Regression model**, a **Flask API**, and a **web-based frontend** for user interaction. The model is trained using a dataset of Bangalore home prices, and it predicts property values based on features like square footage, number of bedrooms, and location.

## Features
- **Data Preprocessing** – Cleaning, handling missing values, and removing outliers  
- **Feature Engineering** – Dimensionality reduction and categorical encoding  
- **Model Training** – Linear Regression with **Scikit-learn**, optimized using **GridSearchCV**  
- **Model Evaluation** – Performance testing using **K-Fold Cross Validation**  
- **Flask API** – Serves predictions in real-time  
- **Interactive Web Interface** – Built using **HTML, CSS, and JavaScript**  
- **Scalable & Extendable** – Can be improved with more ML models and cloud integration  

## Technologies Used
- **Python** – Core language for data processing and model building  
- **Pandas & NumPy** – Data cleaning and manipulation  
- **Matplotlib & Seaborn** – Data visualization and analysis  
- **Scikit-learn** – Machine learning model training and evaluation  
- **Flask** – API for model integration  
- **HTML, CSS, JavaScript** – Frontend for user interaction  
- **Jupyter Notebook, VS Code, PyCharm** – Development environments  

## Dataset
The model is trained on a **Bangalore home prices dataset** sourced from Kaggle. It includes features such as:  
- **Total square feet area**  
- **Number of bedrooms & bathrooms**  
- **Location of the property**  
- **Price per square foot**  
  
## Usage
1. Enter property details (**square feet, number of bedrooms, etc.**).  
2. Click the **Predict** button to fetch results from the **Flask API**.  
3. View the **estimated price instantly**.  
