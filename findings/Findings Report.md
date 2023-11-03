TELCO CUSTOMER CHURN ANALYSIS FINDINGS

INTRODUCTION
In this analysis, I explored the Telco customer churn dataset to understand the factors that influence customer churn in the telecom industry. My analysis includes data preprocessing, visualizations, and feature importance analysis to identify the most influential factors.

Data Preprocessing:
I started the analysis by loading the Telco customer churn dataset and addressing missing values to ensure the dataset's quality. Missing values were imputed appropriately.

EXPLORATORY DATA ANALYSIS (EDA)
Customer Churn Distribution:
I began our EDA by visualizing the distribution of customer churn. The countplot showed that customer churn is imbalanced, with more non-churned customers than churned customers.

Please refer to the Distribution of Customer Churn Chart "Distribution of Customer Churn.png" in the "charts" directory.

Correlation Matrix:
I computed the correlation matrix to understand the relationships between numerical features. This analysis helps identify any multicollinearity that may affect the model. Features like "Total Charges," "Monthly Charges," and "Tenure" showed significant correlations.

Please refer to the Correlation Matrix Chart "Correlation Matrix.png" in the "charts" directory.

PREDICTIVE ANALYTIC MODEL
Model Selection: A Random Forest Classifier was chosen as the predictive model due to its effectiveness in handling both categorical and numerical features, and its ability to provide feature importance scores.

Model Purpose: The primary objective of building this predictive analysis model is to identify and forecast customer churn for Telco. Customer churn, or attrition, represents a critical concern for the company, and proactive measures to retain customers are essential. By developing this model to predict churn, Telco can take timely actions to minimize customer attrition, optimize their services, and enhance customer satisfaction.

Model Training: The Random Forest model was trained on the training dataset using a specified number of decision trees (n_estimators=100, random_state=42) for reproducibility.

Performance Metrics: 
Accuracy (0.79): An accuracy of 0.79 means that the model correctly predicted 79% of the instances.

Confusion Matrix:
True Negatives (TN): The model correctly predicted 948 instances where "Churn" is "False."
False Positives (FP): The model incorrectly predicted 88 instances as "Churn" when they were actually "Not Churn."
False Negatives (FN): The model incorrectly predicted 206 instances as "Not Churn" when they were actually "Churn."
True Positives (TP): The model correctly predicted 167 instances as "Churn."

Classification Report:
Precision: For "False," the precision is 0.82, and for "True," it's 0.65.
Recall: For "False," the recall is 0.92, and for "True," it's 0.45.
F1-Score: For "False," the F1-score is 0.87, and for "True," it's 0.53.
Support: For "False," the support is 1036, and for "True," it's 373.

FEATURE IMPORTANCE
Feature Importance Analysis & Chart:
The feature importance chart indicates that the "Total Charges," "Monthly Charges," and "Tenure" features have the highest influence on predicting customer churn. 

Please refer to the Feature Importance Chart "Feature Importance.png" in the "charts" directory.

Let's interpret the importance of these features and discuss actionable insights:

Total Charges:
- Customers with higher total charges are less likely to churn.
- Consider introducing loyalty or rewards programs to incentivize long-term customers to stay.
- Offer discounts or promotions to encourage customers to increase their total spending.

Monthly Charges:
- High monthly charges play a significant role in churn.
- Analyze the pricing structure and competitiveness of monthly charges.
- Offer personalized packages or discounts to customers with high monthly charges to retain them.
- Consider bundling services to reduce overall costs for customers.

Tenure:
- Long-term customers are less likely to churn.
- Focus on retaining long-term customers.
- Offer exclusive benefits to loyal customers to strengthen their loyalty.
- Implement targeted retention strategies for customers in the early stages of their tenure.

CONCLUSION
This analysis provides valuable insights into factors influencing customer churn in the telecom industry. The findings and actionable insights can help the telecom company take proactive measures to reduce churn, improve customer service, and optimize pricing strategies.

RECOMMENDATIONS
1) Implement loyalty and rewards programs to retain long-term customers who have higher total charges.

2) Analyze the pricing structure and competitiveness of monthly charges to ensure they align with customer expectations.

3) Offer personalized packages and discounts to customers with high monthly charges to retain them.

4) Focus on retaining long-term customers by providing exclusive benefits to strengthen their loyalty.

5) Implement targeted retention strategies for customers in the early stages of their tenure to prevent churn.

By implementing these recommendations, the telecom company can work towards reducing customer churn and improving overall customer satisfaction.


For a detailed technical analysis, please refer to the Jupyter Notebook "analysis.ipynb" in the "notebooks" directory.

For the feature importance chart and correlation matrix visuals, please refer to the "charts" directory.

This report summarizes the key findings and insights from our Telco customer churn analysis.