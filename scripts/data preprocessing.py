## Data Preprocessing

Data preprocessing is an essential step in any data analysis project. I handle missing values, encode categorical variables, and perform any necessary data transformations.

# Check for missing values
missing_values = data.isnull().sum()

# Check for duplicates and remove them
data.drop_duplicates(inplace=True)

# Convert Totalcharges column to numeric (if not already)
data['Totalcharges'] = pd.to_numeric(data['Totalcharges'], errors='coerce')

# Remove customer ID column (not useful for prediction)
data.drop('Customerid', axis=1, inplace=True)

## Actionable insight: I found 11 missing values in the "Totalcharges" column. We need to decide how to handle these missing values.

# Handling missing values
from sklearn.impute import SimpleImputer

# Create an imputer instance
imputer = SimpleImputer(strategy='median')

# Define columns with missing values
columns_with_missing = ["Totalcharges"]

# Apply the imputer to fill missing values
data[columns_with_missing] = imputer.fit_transform(data[columns_with_missing])

# Define the list of columns to be one-hot encoded
columns_to_encode = ['Gender', 'Partner', 'Dependents', 'Phoneservice', 'Multiplelines', 
                     'Internetservice', 'Onlinesecurity', 'Onlinebackup', 'Deviceprotection', 
                     'Techsupport', 'Streamingtv', 'Streamingmovies', 'Contract', 'Paperlessbilling', 'Paymentmethod']

# Perform one-hot encoding
data_encoded = pd.get_dummies(data, columns=columns_to_encode)

# Drop the original categorical columns
data_encoded = data_encoded.drop(columns=columns_to_encode)

# Display the first few rows of the encoded dataset
print(data_encoded.head())

# Scale numeric features
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data[['Tenure', 'Monthlycharges', 'Totalcharges']] = scaler.fit_transform(data[['Tenure', 'Monthlycharges', 'Totalcharges']])