import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load dataset from CSV
df = pd.read_csv('Dataset/product_dataset.csv')

# Ensure 'num1', 'num2', and 'Products' columns exist in the dataset
if not {'num1', 'num2', 'Products'}.issubset(df.columns):
    raise ValueError("Dataset must contain 'num1', 'num2', and 'Products' columns.")

# Features (num1, num2) and target (Products)
X = df[["num1", "num2"]]
y = df["Products"]

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)

# Output results
print(f"Mean Squared Error: {mse}")

# Example prediction for new data
num1, num2 = 10, 20
predicted_product = model.predict([[num1, num2]])
print(f"Predicted Product for num1={num1} and num2={num2}: {predicted_product[0]}")
