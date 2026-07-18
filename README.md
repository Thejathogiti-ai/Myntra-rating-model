🛍️ Myntra Product Rating Prediction using Machine Learning

Project Overview

This project presents an end-to-end Machine Learning pipeline developed to predict whether a Myntra product is likely to receive a high or low customer rating based on product attributes. The project leverages exploratory data analysis, feature engineering, predictive modeling, and deployment through a Streamlit application to deliver an interactive user experience.

🔗 GitHub Repository: https://github.com/Thejathogiti-ai/Myntra-rating-model

🔗 Live Streamlit Application: https://myntra-rating-model-c8uo4myp38pjrzq8gbkcnm.streamlit.app/

# ![Myntra Streamlit App](Myntra app.png)

---

Business Objective

Customer ratings significantly influence purchasing decisions in e-commerce. The objective of this project is to develop a machine learning model capable of predicting product ratings using pricing, discount, product category, brand, and customer engagement features. Such predictive models can support product analysis, merchandising strategies, and decision-making in online retail environments.

---

Dataset

The project utilizes a scraped Myntra product dataset containing approximately 52,000+ records with product-related information.

Features include:

- Brand Name
- Product Description
- Fashion Category
- Price
- MRP
- Discount Percentage
- Number of Ratings

Additional analytical features such as Sales and Revenue were engineered during the exploratory phase to support business-oriented analysis.

---

Exploratory Data Analysis (EDA)

Exploratory Data Analysis was leveraged to understand the structure, quality, and distribution of the dataset before model development.

The analysis included:

- Data inspection and validation
- Missing value analysis
- Descriptive statistical analysis
- Brand-wise product distribution
- Price and MRP distribution
- Revenue analysis
- Price segmentation
- Identification of high-value products

A custom Price Category feature was engineered to classify products into:

- Economical
- Affordable
- Premium
- Luxury

These insights helped establish a better understanding of the dataset before model training.

---

Data Preprocessing & Feature Engineering

The dataset was prepared using multiple preprocessing techniques prior to model development.

Key preprocessing steps included:

- Data cleaning
- Feature selection
- Creation of Sales and Revenue features
- Price Category engineering
- Encoding categorical variables
- Train-Test Split

The processed dataset served as the foundation for training the machine learning models.

---

Model Development

Multiple machine learning classification models were developed and evaluated to identify the most suitable approach for rating prediction.

Models employed:

- Logistic Regression
- Decision Tree Classifier

Each model was trained using the engineered features and assessed based on predictive performance.

---

Model Evaluation

The comparative evaluation indicated that the Decision Tree Classifier demonstrated stronger predictive performance than Logistic Regression for this dataset.

Consequently, the Decision Tree model was selected as the final production model, serialized using Pickle, and deployed for real-time inference.

---

Streamlit Deployment

To enable interactive predictions, the trained model was deployed using Streamlit.

The application allows users to input product attributes such as:

- Price
- MRP
- Discount Percentage
- Number of Ratings
- Brand
- Product Description
- Fashion Category

Based on these inputs, the deployed model predicts whether the product is likely to receive a High Rating or Low Rating.

---

Repository Structure

📂 Myntra-rating-model
│
├── Myntra-Logreg&DT[Theja].ipynb
├── app.py
├── model.pkl
├── myntra_dataset_ByScraping.xlsx
├── requirements.txt
└── README.md

---

Technology Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Pickle
- Jupyter Notebook

---

Future Enhancements

Future improvements for this project include:

- Hyperparameter tuning
- Ensemble learning models
- Advanced feature engineering
- Cross-validation for improved model robustness
- Automated model retraining pipeline
- Deployment using cloud platforms

---

Conclusion

This project demonstrates an end-to-end Machine Learning workflow, beginning with exploratory data analysis and feature engineering, progressing through predictive model development and evaluation, and culminating in deployment through a Streamlit application. It reflects the practical application of data science techniques to solve a real-world predictive analytics problem while emphasizing reproducibility, model evaluation, and user accessibility.












