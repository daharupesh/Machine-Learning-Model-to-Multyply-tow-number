# Product Sales Prediction using Linear Regression

This project demonstrates how to use Linear Regression to predict product sales based on two numerical features (`num1` and `num2`). The model is trained on a dataset and evaluated using the Mean Squared Error (MSE) metric. This repository contains the implementation of data preprocessing, training, and model evaluation.

## Dataset

The dataset should contain three columns:
- `num1`: A numerical feature.
- `num2`: Another numerical feature.
- `Products`: The target column representing product sales.

You can load your dataset into the `Dataset` folder as `product_dataset.csv`.

## Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.x
- Pandas
- Scikit-learn

Install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

### `requirements.txt`

```
pandas
scikit-learn
```

## Project Structure

```
├── Dataset/
│   └── product_dataset.csv    # Your dataset should be placed here
├── README.md                  # Project documentation
├── main.py                    # Code to train and test the linear regression model
└── requirements.txt           # List of required Python libraries
```

## Code Description

The `main.py` script performs the following tasks:
1. Loads the dataset from the `Dataset/product_dataset.csv` file.
2. Splits the data into training and testing sets.
3. Trains a Linear Regression model using `num1` and `num2` as features to predict `Products`.
4. Evaluates the model using Mean Squared Error (MSE).
5. Predicts the `Products` value for a new set of input values.

## Usage

 Run the script:

```bash
python main.py
```

### Sample Output

```
Mean Squared Error: 12.3456
Predicted Product for num1=10 and num2=20: 123.456
```

## Example Prediction

The model can be used to predict product sales for new input values of `num1` and `num2`. For example:

```python
# Example prediction for num1=10 and num2=20
predicted_product = model.predict([[10, 20]])
```

This will output the predicted product sales for the provided input.
